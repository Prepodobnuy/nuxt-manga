from sqlalchemy.orm import Session


def get_by_id(cls, session: Session, id: int):
    try:
        return session.query(cls).filter(cls.id == id).first()
    except Exception:
        return None


def get_by_uuid(cls, session: Session, uuid: str):
    try:
        return session.query(cls).filter(cls.uuid == uuid).first()
    except Exception:
        return None