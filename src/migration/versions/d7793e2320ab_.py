"""empty message

Revision ID: d7793e2320ab
Revises: 1e6cac02527a
Create Date: 2024-02-18 22:44:19.344240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd7793e2320ab'
down_revision: Union[str, None] = '1e6cac02527a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('category', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'updated_at')
    op.drop_column('category', 'created_at')
    # ### end Alembic commands ###
