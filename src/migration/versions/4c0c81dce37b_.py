"""empty message

Revision ID: 4c0c81dce37b
Revises: db51af5d7b22
Create Date: 2024-02-27 22:52:11.332995

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c0c81dce37b'
down_revision: Union[str, None] = 'db51af5d7b22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('belts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(precision=10), nullable=True),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('length', sa.String(length=50), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('width', sa.String(length=50), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('buckles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cartholders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('insoles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purse',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(precision=10), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('material', sa.String(length=100), nullable=True),
    sa.Column('size', sa.String(length=100), nullable=True),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('url_image', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    sa.Column('product_type_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['product_type_id'], ['product_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('wallets')
    op.drop_table('purse')
    op.drop_table('product_type')
    op.drop_table('insoles')
    op.drop_table('category')
    op.drop_table('cartholders')
    op.drop_table('buckles')
    op.drop_table('belts')
    # ### end Alembic commands ###
