"""empty message

Revision ID: 41cb4c084ba7
Revises: 40e09df5570d
Create Date: 2019-03-25 16:21:51.544613

"""

# revision identifiers, used by Alembic.
revision = '41cb4c084ba7'
down_revision = '40e09df5570d'
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
    ### commands auto generated by Alembic - please adjust! ###
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    op.add_column(u'assa_impression_stats_daily', sa.Column('loaded', sa.Integer(), server_default='0', nullable=True))
    ### end Alembic commands ###


def downgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    op.drop_column(u'assa_impression_stats_daily', 'loaded')
    ### end Alembic commands ###

