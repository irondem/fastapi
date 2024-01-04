"""add content column to posts table

Revision ID: 08b5eb43fa61
Revises: acba136b9f43
Create Date: 2024-01-03 16:14:31.061418

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08b5eb43fa61'
down_revision: Union[str, None] = 'acba136b9f43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
