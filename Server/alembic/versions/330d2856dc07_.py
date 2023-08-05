"""empty message

Revision ID: 330d2856dc07
Revises: 146b6bd2d460
Create Date: 2023-08-05 00:17:54.341721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '330d2856dc07'
down_revision = '146b6bd2d460'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cart_items_couponId_fkey', 'cart_items', type_='foreignkey')
    op.drop_column('cart_items', 'couponId')
    op.add_column('users', sa.Column('couponId', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'coupons', ['couponId'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'couponId')
    op.add_column('cart_items', sa.Column('couponId', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('cart_items_couponId_fkey', 'cart_items', 'coupons', ['couponId'], ['id'])
    # ### end Alembic commands ###