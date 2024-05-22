"""migrate models

Revision ID: 9272bfe463b8
Revises: 294c910a678b
Create Date: 2024-05-21 16:43:52.724074

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9272bfe463b8'
down_revision: Union[str, None] = '294c910a678b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('streams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_streams_id'), 'streams', ['id'], unique=False)
    op.create_index(op.f('ix_streams_title'), 'streams', ['title'], unique=False)
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('content', sa.LargeBinary(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_videos_id'), 'videos', ['id'], unique=False)
    op.create_index(op.f('ix_videos_title'), 'videos', ['title'], unique=False)
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    op.create_table('subscriptions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('stream_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], ['streams.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscriptions_id'), 'subscriptions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscriptions_id'), table_name='subscriptions')
    op.drop_table('subscriptions')
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_table('comments')
    op.drop_index(op.f('ix_videos_title'), table_name='videos')
    op.drop_index(op.f('ix_videos_id'), table_name='videos')
    op.drop_table('videos')
    op.drop_index(op.f('ix_streams_title'), table_name='streams')
    op.drop_index(op.f('ix_streams_id'), table_name='streams')
    op.drop_table('streams')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###