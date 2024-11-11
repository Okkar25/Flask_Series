"""empty message

Revision ID: 5d8afb3f86e5
Revises: 4850f4fdedda
Create Date: 2024-11-04 15:46:24.321804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d8afb3f86e5'
down_revision = '4850f4fdedda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pid', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), sa.Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.drop_column('age')
        batch_op.drop_column('pid')

    # ### end Alembic commands ###