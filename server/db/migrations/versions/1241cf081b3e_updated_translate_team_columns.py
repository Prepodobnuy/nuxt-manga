"""Updated translate_team columns

Revision ID: 1241cf081b3e
Revises: 169d9534de5b
Create Date: 2025-05-05 20:32:01.329419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1241cf081b3e'
down_revision: Union[str, None] = '169d9534de5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'translate_team', ['title'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'translate_team', type_='unique')
    # ### end Alembic commands ###
