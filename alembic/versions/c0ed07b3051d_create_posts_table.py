"""create posts table

Revision ID: c0ed07b3051d
Revises: 
Create Date: 2026-10-07 21:42:19.627434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ed07b3051d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column("title", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
