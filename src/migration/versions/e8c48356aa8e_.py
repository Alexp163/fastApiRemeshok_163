"""empty message

Revision ID: e8c48356aa8e
Revises: 35eff099d351
Create Date: 2024-03-28 20:39:37.112426

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8c48356aa8e'
down_revision: Union[str, None] = '35eff099d351'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('descript_text', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('descript_text', sa.Column('updated_at', sa.DateTime(), nullable=True))
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
    op.drop_column('descript_text', 'updated_at')
    op.drop_column('descript_text', 'created_at')
    # ### end Alembic commands ###
