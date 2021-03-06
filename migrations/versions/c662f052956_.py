"""empty message

Revision ID: c662f052956
Revises: 52c5946188c4
Create Date: 2016-08-29 10:00:57.532481

"""

# revision identifiers, used by Alembic.
revision = 'c662f052956'
down_revision = '52c5946188c4'
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
    op.add_column('activity_stream_events_daily', sa.Column('metadata_source', sa.String(length=64), nullable=True))
    op.add_column('activity_stream_performance_daily', sa.Column('metadata_source', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    import os
    if os.environ.get("SPLICE_IGNORE_REDSHIFT", "") == "true":
        return
    op.drop_column('activity_stream_performance_daily', 'metadata_source')
    op.drop_column('activity_stream_events_daily', 'metadata_source')
    ### end Alembic commands ###

