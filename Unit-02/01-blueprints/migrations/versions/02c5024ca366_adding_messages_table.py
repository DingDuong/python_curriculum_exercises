"""adding messages table

Revision ID: 02c5024ca366
Revises: a40d037bd01f
Create Date: 2017-11-30 19:42:43.100357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02c5024ca366'
down_revision = 'a40d037bd01f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###