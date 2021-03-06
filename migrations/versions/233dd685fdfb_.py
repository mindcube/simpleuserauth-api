"""empty message

Revision ID: 233dd685fdfb
Revises: None
Create Date: 2016-02-24 23:37:24.721162

"""

# revision identifiers, used by Alembic.
revision = '233dd685fdfb'
down_revision = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=True),
    sa.Column('token', sa.String(length=512), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
