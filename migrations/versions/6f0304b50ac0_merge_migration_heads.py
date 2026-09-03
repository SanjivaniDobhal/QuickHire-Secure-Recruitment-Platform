"""merge migration heads

Revision ID: 6f0304b50ac0
Revises: f90ebc3384df, abc123456789
Create Date: 2026-09-03 01:02:24.958443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f0304b50ac0'
down_revision = ('f90ebc3384df', 'abc123456789')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
