"""empty message

Revision ID: 38b08f85aab8
Revises: 4587bf9b5b61
Create Date: 2019-10-07 23:26:09.933509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38b08f85aab8'
down_revision = '4587bf9b5b61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emails')
    # ### end Alembic commands ###