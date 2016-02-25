"""empty message

Revision ID: be04edfbb1c2
Revises: 0c20704b185f
Create Date: 2016-02-25 01:54:51.525115

"""

# revision identifiers, used by Alembic.
revision = 'be04edfbb1c2'
down_revision = '0c20704b185f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'token')
    op.drop_column('user', 'token_expiration')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token_expiration', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('token', sa.VARCHAR(length=512), autoincrement=False, nullable=True))
    ### end Alembic commands ###