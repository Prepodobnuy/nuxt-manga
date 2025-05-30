"""upgraded translate_team

Revision ID: dfd2be83dbf7
Revises: e3c2b9d93059
Create Date: 2025-05-11 10:32:53.374721

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfd2be83dbf7'
down_revision: Union[str, None] = 'e3c2b9d93059'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('translate_team', sa.Column('owner_uuid', sa.String(), nullable=False))
    op.drop_constraint('translate_team_owner_fkey', 'translate_team', type_='foreignkey')
    op.create_foreign_key(None, 'translate_team', 'user', ['owner_uuid'], ['uuid'])
    op.drop_column('translate_team', 'owner')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('translate_team', sa.Column('owner', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'translate_team', type_='foreignkey')
    op.create_foreign_key('translate_team_owner_fkey', 'translate_team', 'user', ['owner'], ['uuid'])
    op.drop_column('translate_team', 'owner_uuid')
    # ### end Alembic commands ###
