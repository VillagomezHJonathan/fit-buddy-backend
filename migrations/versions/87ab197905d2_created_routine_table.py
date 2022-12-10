"""created routine table

Revision ID: 87ab197905d2
Revises: 60335718a3f1
Create Date: 2022-12-10 11:32:39.667770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87ab197905d2'
down_revision = '60335718a3f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('routines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('routines')
    # ### end Alembic commands ###
