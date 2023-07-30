"""empty message

Revision ID: 2e646dfa6db7
Revises: 18915931b1a1
Create Date: 2023-07-29 14:09:50.648018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e646dfa6db7'
down_revision = '18915931b1a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('sold', sa.Integer(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('brand', sa.String(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=False),
    sa.Column('fname', sa.String(), nullable=False),
    sa.Column('lname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('mobile', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('blocked', sa.Boolean(), nullable=False),
    sa.Column('refreshToken', sa.String(), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile')
    )
    op.create_table('ratings',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('userId', 'productId')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ratings')
    op.drop_table('users')
    op.drop_table('products')
    # ### end Alembic commands ###
