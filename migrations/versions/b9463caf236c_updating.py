"""updating 

Revision ID: b9463caf236c
Revises: 465d1c566e14
Create Date: 2024-01-24 12:45:47.812206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9463caf236c'
down_revision = '465d1c566e14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('users_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workouts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('users_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key(None, 'users', ['users_id'], ['id'])

    # ### end Alembic commands ###
