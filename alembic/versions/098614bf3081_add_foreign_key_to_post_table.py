"""add foreign-key to post table

Revision ID: 098614bf3081
Revises: e41d4ca00e03
Create Date: 2026-10-07 22:03:32.913637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '098614bf3081'
down_revision = 'e41d4ca00e03'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
