"""empty message

Revision ID: a29b4778fdf1
Revises: 65cd37b56ca9
Create Date: 2019-06-18 17:56:31.626659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from apigateway import populate_database

revision = 'a29b4778fdf1'
down_revision = '65cd37b56ca9'
branch_labels = None
depends_on = None


def upgrade():
    populate_database()


def downgrade():
    pass
