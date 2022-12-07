"""create posts table

Revision ID: 0a13843f5ce6
Revises: 
Create Date: 2022-12-07 14:32:36.669693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a13843f5ce6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', 
        sa.Column('id', sa.Integer, nullable=False, primary_key = True),
        sa.Column('title', sa.String , nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
