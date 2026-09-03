"""add location coordinates

Revision ID: f419fe194f25
Revises: 771eab19334d
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f419fe194f25'
down_revision = '771eab19334d'
branch_labels = None
depends_on = None


def upgrade():
    # Add latitude and longitude to employers
    op.add_column(
        'employers',
        sa.Column('latitude', sa.Float(), nullable=True)
    )

    op.add_column(
        'employers',
        sa.Column('longitude', sa.Float(), nullable=True)
    )

    # Add latitude and longitude to jobs
    op.add_column(
        'jobs',
        sa.Column('latitude', sa.Float(), nullable=True)
    )

    op.add_column(
        'jobs',
        sa.Column('longitude', sa.Float(), nullable=True)
    )

    # Add latitude and longitude to jobseekers
    op.add_column(
        'jobseekers',
        sa.Column('latitude', sa.Float(), nullable=True)
    )

    op.add_column(
        'jobseekers',
        sa.Column('longitude', sa.Float(), nullable=True)
    )


def downgrade():
    # Remove jobseeker coordinates
    op.drop_column('jobseekers', 'longitude')
    op.drop_column('jobseekers', 'latitude')

    # Remove job coordinates
    op.drop_column('jobs', 'longitude')
    op.drop_column('jobs', 'latitude')

    # Remove employer coordinates
    op.drop_column('employers', 'longitude')
    op.drop_column('employers', 'latitude')