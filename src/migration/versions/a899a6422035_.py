"""empty message

Revision ID: a899a6422035
Revises: de63bcb909ba
Create Date: 2024-02-18 23:35:31.269937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a899a6422035'
down_revision: Union[str, None] = 'de63bcb909ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Float(precision=10), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('width', sa.String(length=50), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_type')
    op.drop_table('product')
    # ### end Alembic commands ###
