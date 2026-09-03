"""add missing application tables

Revision ID: e591c042a6b6
Revises: f419fe194f25
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e591c042a6b6'
down_revision = 'f419fe194f25'
branch_labels = None
depends_on = None


def upgrade():

    # ---------------------------------------------------------
    # 1. Reviews
    # ---------------------------------------------------------
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('reviewer_id', sa.Integer(), nullable=False),
        sa.Column('reviewee_id', sa.Integer(), nullable=False),
        sa.Column('job_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(
            ['reviewer_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['reviewee_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['job_id'],
            ['jobs.id'],
            ondelete='CASCADE'
        ),

        sa.PrimaryKeyConstraint('id')
    )


    # ---------------------------------------------------------
    # 2. Direct Hires
    # ---------------------------------------------------------
    op.create_table(
        'direct_hires',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('employer_id', sa.Integer(), nullable=False),
        sa.Column('jobseeker_id', sa.Integer(), nullable=False),
        sa.Column('hired_at', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(length=20), nullable=True),

        sa.ForeignKeyConstraint(
            ['employer_id'],
            ['employers.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['jobseeker_id'],
            ['jobseekers.id'],
            ondelete='CASCADE'
        ),

        sa.PrimaryKeyConstraint('id')
    )


    # ---------------------------------------------------------
    # 3. Chat Rooms
    # ---------------------------------------------------------
    op.create_table(
        'chat_rooms',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('employer_id', sa.Integer(), nullable=False),
        sa.Column('jobseeker_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('last_message_at', sa.DateTime(), nullable=True),

        sa.ForeignKeyConstraint(
            ['employer_id'],
            ['employers.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['jobseeker_id'],
            ['jobseekers.id'],
            ondelete='CASCADE'
        ),

        sa.PrimaryKeyConstraint('id')
    )


    # ---------------------------------------------------------
    # 4. Chat Messages
    # ---------------------------------------------------------
    op.create_table(
        'chat_messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('room_id', sa.Integer(), nullable=False),
        sa.Column('sender_id', sa.Integer(), nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('sent_at', sa.DateTime(), nullable=True),
        sa.Column('is_read', sa.Boolean(), nullable=True),

        sa.ForeignKeyConstraint(
            ['room_id'],
            ['chat_rooms.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['sender_id'],
            ['users.id'],
            ondelete='CASCADE'
        ),

        sa.PrimaryKeyConstraint('id')
    )


def downgrade():

    # Drop child table first
    op.drop_table('chat_messages')

    # Then chat rooms
    op.drop_table('chat_rooms')

    # Then direct hires
    op.drop_table('direct_hires')

    # Finally reviews
    op.drop_table('reviews')