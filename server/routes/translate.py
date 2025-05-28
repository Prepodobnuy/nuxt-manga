from datetime import datetime, timezone
from io import BytesIO
import json
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from PIL import Image
from sqlalchemy.orm import query
from db.session_fabric import connection, get_session
from models.translate.translate_team import TranslateTeam
from models.translate.translate_team_member import TranslateTeamMember
from models.user.user import User
from modules.auth import get_moder, get_not_muted
from schemas.translate import (
    TranslateTeamMemberScheme,
    TranslateTeamPostScheme,
    TranslateTeamScheme,
)


router = APIRouter()


async def user_in_team(
    uuid: str,
    session: AsyncSession,
) -> bool:
    query = select(TranslateTeam).where(TranslateTeam.owner_uuid == uuid)
    squery = select(TranslateTeamMember).where(TranslateTeamMember.uuid == uuid)
    if (await session.execute(query)).scalar_one_or_none() is not None:
        return True
    if (await session.execute(squery)).scalar_one_or_none() is not None:
        return True
    return False


async def user_owns_team(
    uuid: str,
    session: AsyncSession,
) -> bool:
    query = select(TranslateTeam).where(TranslateTeam.owner_uuid == uuid)
    if (await session.execute(query)).scalar_one_or_none() is not None:
        return True
    return False


async def user_own_team(
    uuid: str,
    session: AsyncSession,
) -> TranslateTeam | None:
    query = select(TranslateTeam).where(TranslateTeam.owner_uuid == uuid)
    return (await session.execute(query)).scalar_one_or_none()


@connection
async def _get_pending(session: AsyncSession | None = None) -> list[TranslateTeam]:
    assert session is not None

    query = select(TranslateTeam).where(TranslateTeam.approved == False)
    return list((await session.execute(query)).scalars().all())


@connection
async def _get_approved(session: AsyncSession | None = None) -> list[TranslateTeam]:
    assert session is not None

    query = select(TranslateTeam).where(TranslateTeam.approved == True)
    return list((await session.execute(query)).scalars().all())


@connection
async def _get_members(
    team: TranslateTeam, session: AsyncSession | None = None
) -> list[TranslateTeamMember]:
    assert session is not None

    query = select(TranslateTeamMember).where(TranslateTeamMember.team_id == team.id)
    return list((await session.execute(query)).scalars().all())


async def _team_to_scheme(team: TranslateTeam):
    accepted_members = []
    pending_members = []

    for member in await _get_members(team=team):
        if member.accepted:
            accepted_members.append(
                TranslateTeamMemberScheme(
                    uuid=member.uuid,
                    team_id=member.team_id,
                    accepted=True,
                )
            )
            continue
        pending_members.append(
            TranslateTeamMemberScheme(
                uuid=member.uuid,
                team_id=member.team_id,
                accepted=False,
            )
        )

    return TranslateTeamScheme(
        id=team.id,
        owner_uuid=team.owner_uuid,
        title=team.title,
        description=team.description,
        approved=team.approved,
        accepted_members=accepted_members,
        unaccepted_members=pending_members,
    )


@router.get("/pending")
async def get_pending_translate_teams(
    user: User = Depends(get_moder),
) -> list[TranslateTeamScheme]:
    res = []

    for t in await _get_pending():
        res.append(await _team_to_scheme(team=t))

    return res


@router.get("/{id}")
async def get_translate_team(
    id: int,
    session: AsyncSession = Depends(get_session),
) -> TranslateTeamScheme:
    query = select(TranslateTeam).where(TranslateTeam.id == id)

    async with session:
        team = (await session.execute(query)).scalar_one_or_none()

        if team is None:
            raise HTTPException(404)

        return await _team_to_scheme(team=team)


@router.post("/")
async def create_translate_team(
    file: UploadFile = File(...),
    scheme: str = Form(...),
    user: User = Depends(get_not_muted),
    session: AsyncSession = Depends(get_session),
):
    if file.content_type is None:
        raise HTTPException(415, "no file supplied")
    if not file.content_type.startswith("image/"):
        raise HTTPException(415, "file is not an image")
    try:
        parsed = TranslateTeamPostScheme(**json.loads(scheme))
    except Exception:
        raise HTTPException(400, "failed to parse scheme")

    query = select(TranslateTeam).where(TranslateTeam.owner_uuid == user.uuid)
    squery = select(TranslateTeamMember).where(TranslateTeamMember.uuid == user.uuid)
    tquery = select(TranslateTeam).where(TranslateTeam.title == parsed.title)

    async with session:
        try:
            if await user_in_team(uuid=user.uuid, session=session):
                raise HTTPException(400, "user in team already")
            if (await session.execute(tquery)).scalar_one_or_none() is not None:
                raise HTTPException(400, "title taken")

            content = await file.read()

            team = TranslateTeam(
                owner_uuid=user.uuid,
                title=parsed.title,
                pfp=content,
            )

            session.add(team)

            await session.commit()

        except HTTPException as e:
            print(e)
            await session.rollback()
            raise e

        except Exception as e:
            print(e)
            await session.rollback()
            raise HTTPException(500)

    pass


@router.post("/{id}/askjoin")
async def ask_to_join_translate_team(
    id: int,
    user: User = Depends(get_not_muted),
    session: AsyncSession = Depends(get_session),
):
    query = select(TranslateTeam).where(TranslateTeam.id == id)

    async with session:
        try:
            if await user_in_team(uuid=user.uuid, session=session):
                raise HTTPException(400)

            team = (await session.execute(query)).scalar_one_or_none()

            if team is None:
                raise HTTPException(404)

            member = TranslateTeamMember(uuid=user.uuid, team_id=team.id)

            session.add(member)
            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception:
            await session.rollback()
            raise HTTPException(500)


@router.post("/{uuid}/accept")
async def accept_join(
    uuid: str,
    user: User = Depends(get_not_muted),
    session: AsyncSession = Depends(get_session),
):
    query = lambda id: select(TranslateTeamMember).where(
        TranslateTeamMember.uuid == uuid, TranslateTeamMember.team_id == id
    )

    async with session:
        try:
            team = await user_own_team(uuid=user.uuid, session=session)
            if team is None:
                raise HTTPException(403)

            member = (await session.execute(query(team.id))).scalar_one_or_none()
            if member is None:
                raise HTTPException(404)

            member.accepted = True

            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception:
            await session.rollback()
            raise HTTPException(500)


@router.delete("/{uuid}/decline")
async def delete_translate_team_member(
    uuid: str,
    user: User = Depends(get_not_muted),
    session: AsyncSession = Depends(get_session),
):
    query = lambda id: select(TranslateTeamMember).where(
        TranslateTeamMember.uuid == uuid, TranslateTeamMember.team_id == id
    )

    async with session:
        try:
            team = await user_own_team(uuid=user.uuid, session=session)
            if team is None:
                raise HTTPException(403)

            member = (await session.execute(query(team.id))).scalar_one_or_none()
            if member is None:
                raise HTTPException(404)

            await session.delete(member)
            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception:
            await session.rollback()
            raise HTTPException(500)


@router.delete("/{id}/disapprove")
async def disapprove_translate_team(
    id: int,
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    query = select(TranslateTeam).where(TranslateTeam.id == id)

    async with session:
        try:
            team = (await session.execute(query)).scalar_one_or_none()
            if team is None:
                raise HTTPException(404)

            await session.delete(team)
            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception:
            await session.rollback()
            raise HTTPException(500)


@router.post("/{id}/approve")
async def approve_translate_team(
    id: int,
    user: User = Depends(get_moder),
    session: AsyncSession = Depends(get_session),
):
    query = select(TranslateTeam).where(TranslateTeam.id == id)

    async with session:
        try:
            team = (await session.execute(query)).scalar_one_or_none()
            if team is None:
                raise HTTPException(404)

            team.approved = True
            team.approved_user_uuid = user.uuid

            await session.commit()

        except HTTPException as e:
            await session.rollback()
            raise e

        except Exception:
            await session.rollback()
            raise HTTPException(500)
