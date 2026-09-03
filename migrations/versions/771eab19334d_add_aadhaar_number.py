"""add aadhaar number

Revision ID: 771eab19334d
Revises: 6f0304b50ac0
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771eab19334d'
down_revision = '6f0304b50ac0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users',
        sa.Column('aadhaar_number', sa.String(length=12), nullable=False)
    )

    op.create_unique_constraint(
        'uq_users_aadhaar_number',
        'users',
        ['aadhaar_number']
    )


def downgrade():
    op.drop_constraint(
        'uq_users_aadhaar_number',
        'users',
        type_='unique'
    )

    op.drop_column(
        'users',
        'aadhaar_number'
    )