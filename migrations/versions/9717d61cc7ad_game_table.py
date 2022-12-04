"""game table

Revision ID: 9717d61cc7ad
Revises: 
Create Date: 2022-12-04 10:29:42.064911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9717d61cc7ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('url', sa.String(length=128), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=False),
    sa.Column('published', sa.Boolean(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_game_author'), 'game', ['author'], unique=False)
    op.create_index(op.f('ix_game_description'), 'game', ['description'], unique=False)
    op.create_index(op.f('ix_game_name'), 'game', ['name'], unique=False)
    op.create_index(op.f('ix_game_url'), 'game', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_game_url'), table_name='game')
    op.drop_index(op.f('ix_game_name'), table_name='game')
    op.drop_index(op.f('ix_game_description'), table_name='game')
    op.drop_index(op.f('ix_game_author'), table_name='game')
    op.drop_table('game')
    # ### end Alembic commands ###