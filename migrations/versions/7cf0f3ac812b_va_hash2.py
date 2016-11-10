"""va-hash2

Revision ID: 7cf0f3ac812b
Revises: 374a18eaeac7
Create Date: 2016-11-10 14:06:34.347882

"""

# revision identifiers, used by Alembic.
revision = '7cf0f3ac812b'
down_revision = '374a18eaeac7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # op.drop_column('users', 'new_email')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # op.add_column('users', sa.Column('new_email', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###