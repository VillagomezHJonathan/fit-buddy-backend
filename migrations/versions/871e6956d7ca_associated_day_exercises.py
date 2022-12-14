"""associated day exercises

Revision ID: 871e6956d7ca
Revises: f951d4e5170f
Create Date: 2022-12-10 16:20:46.054558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '871e6956d7ca'
down_revision = 'f951d4e5170f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('days_exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('routine_id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('day_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['day_id'], ['days.id'], ),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.ForeignKeyConstraint(['routine_id'], ['routines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('days_exercises')
    # ### end Alembic commands ###
