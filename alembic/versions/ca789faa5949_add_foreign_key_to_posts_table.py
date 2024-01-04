"""add foreign-key to posts table

Revision ID: ca789faa5949
Revises: cace714ee4cf
Create Date: 2024-01-04 12:21:24.063243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca789faa5949'
down_revision: Union[str, None] = 'cace714ee4cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name=	"posts")
    op.drop_column('posts', 'owner_id')
    pass
