"""comm

Revision ID: c8786fba6da5
Revises: 26f6759122a9
Create Date: 2024-05-22 18:00:28.303415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8786fba6da5'
down_revision: Union[str, None] = '26f6759122a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('videos', 'status')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('videos', sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
