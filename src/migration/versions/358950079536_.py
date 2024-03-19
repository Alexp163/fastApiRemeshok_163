"""empty message

Revision ID: 358950079536
Revises: dc25046ded42
Create Date: 2024-03-18 23:17:10.497331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358950079536'
down_revision: Union[str, None] = 'dc25046ded42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('url', sa.String(length=250), nullable=True))
    op.alter_column('product', 'price',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=10),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'price',
               existing_type=sa.Float(precision=10),
               type_=sa.REAL(),
               existing_nullable=True)
    op.drop_column('product', 'url')
    # ### end Alembic commands ###
