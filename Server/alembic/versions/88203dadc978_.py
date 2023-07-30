"""empty message

Revision ID: 88203dadc978
Revises: 193ba82f64ab
Create Date: 2023-07-28 22:35:03.260803

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '88203dadc978'
down_revision = '193ba82f64ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('createdAt', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('updatedAt', sa.DateTime(), nullable=True))
    op.drop_column('users', 'created')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.drop_column('users', 'updatedAt')
    op.drop_column('users', 'createdAt')
    # ### end Alembic commands ###
