from sqlalchemy import *
from migrate import *

meta = MetaData()

user = Table(
    "user", meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(50)),
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    user.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    user.drop()
