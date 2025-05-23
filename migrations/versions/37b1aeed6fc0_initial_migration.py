"""Initial migration

Revision ID: 37b1aeed6fc0
Revises: 
Create Date: 2025-04-20 01:47:02.406136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b1aeed6fc0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('liked_song',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=400), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_table('user',
    sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('liked_song')
    # ### end Alembic commands ###
