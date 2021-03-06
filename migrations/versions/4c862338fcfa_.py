"""Set default created_at to:
account, channels, distributions, adgroup_sites, tiles

Revision ID: 4c862338fcfa
Revises: 3cc07fb28766
Create Date: 2015-11-04 10:56:03.260356

"""

# revision identifiers, used by Alembic.
revision = '4c862338fcfa'
down_revision = '3cc07fb28766'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    op.alter_column('adgroups', 'created_at', server_default=sa.text(u'now()'))
    op.alter_column('channels', 'created_at', server_default=sa.text(u'now()'))
    op.alter_column('distributions', 'created_at', server_default=sa.text(u'now()'))
    op.alter_column('adgroup_sites', 'created_at', server_default=sa.text(u'now()'))
    op.alter_column('tiles', 'created_at', server_default=sa.text(u'now()'))


def downgrade_():
    op.alter_column('adgroups', 'created_at', server_default=None)
    op.alter_column('channels', 'created_at', server_default=None)
    op.alter_column('distributions', 'created_at', server_default=None)
    op.alter_column('adgroup_sites', 'created_at', server_default=None)
    op.alter_column('tiles', 'created_at', server_default=None)


def upgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###


def downgrade_stats():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###
