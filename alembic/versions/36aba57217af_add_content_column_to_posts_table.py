"""add content column to posts table

Revision ID: 36aba57217af
Revises: 0a13843f5ce6
Create Date: 2022-12-07 21:10:21.660985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36aba57217af'
down_revision = '0a13843f5ce6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
