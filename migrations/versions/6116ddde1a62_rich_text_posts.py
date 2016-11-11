"""rich_text_posts

Revision ID: 6116ddde1a62
Revises: 8ad2ee9d8f86
Create Date: 2016-11-11 14:57:35.771273

"""

# revision identifiers, used by Alembic.
revision = '6116ddde1a62'
down_revision = '8ad2ee9d8f86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
