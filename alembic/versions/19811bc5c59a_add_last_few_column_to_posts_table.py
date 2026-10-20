"""add last few column to posts table

Revision ID: 19811bc5c59a
Revises: 098614bf3081
Create Date: 2026-10-07 22:08:49.777976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19811bc5c59a'
down_revision = '098614bf3081'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
