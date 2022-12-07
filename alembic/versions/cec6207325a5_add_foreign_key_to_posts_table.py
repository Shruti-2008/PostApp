"""add foreign-key to posts table

Revision ID: cec6207325a5
Revises: 385b4e9db361
Create Date: 2022-12-08 00:17:17.715329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec6207325a5'
down_revision = '385b4e9db361'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
