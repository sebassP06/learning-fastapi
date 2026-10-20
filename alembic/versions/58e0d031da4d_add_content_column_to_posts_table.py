"""add content column to posts table

Revision ID: 58e0d031da4d
Revises: c0ed07b3051d
Create Date: 2026-10-07 21:50:54.856554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58e0d031da4d'
down_revision = 'c0ed07b3051d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
