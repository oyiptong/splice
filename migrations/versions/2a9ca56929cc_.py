"""empty message

Revision ID: 2a9ca56929cc
Revises: 159a3bd70527
Create Date: 2018-08-14 16:29:34.580165

"""

# revision identifiers, used by Alembic.
revision = '2a9ca56929cc'
down_revision = '159a3bd70527'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def upgrade_stats():
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'assa_sessions_daily', sa.Column('topsites_search_shortcuts', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade_stats():
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'assa_sessions_daily', 'topsites_search_shortcuts')
    ### end Alembic commands ###

