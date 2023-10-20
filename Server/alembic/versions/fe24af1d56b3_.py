"""empty message

Revision ID: fe24af1d56b3
Revises: 8c0e376cfe7d
Create Date: 2023-10-18 22:02:32.212183

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fe24af1d56b3'
down_revision = '8c0e376cfe7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=False))
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('refresh_token', sa.String(), nullable=True))
    op.add_column('users', sa.Column('pass_reset_token', sa.String(), nullable=True))
    op.add_column('users', sa.Column('pass_reset_token_exp', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('users', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.drop_column('users', 'isAdmin')
    op.drop_column('users', 'createdAt')
    op.drop_column('users', 'updatedAt')
    op.drop_column('users', 'passResetToken')
    op.drop_column('users', 'password')
    op.drop_column('users', 'passResetTokenExp')
    op.drop_column('users', 'refreshToken')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('refreshToken', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('passResetTokenExp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('passResetToken', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('updatedAt', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('createdAt', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('isAdmin', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('users', 'pass_reset_token_exp')
    op.drop_column('users', 'pass_reset_token')
    op.drop_column('users', 'refresh_token')
    op.drop_column('users', 'is_admin')
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###