"""add user table

Revision ID: 385b4e9db361
Revises: 36aba57217af
Create Date: 2022-12-07 21:20:49.183982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '385b4e9db361'
down_revision = '36aba57217af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()') , nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
