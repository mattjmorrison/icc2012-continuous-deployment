from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    email = Column('email', String(128))
    email.create(user)


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    user = Table('user', meta, autoload=True)
    user.c.email.drop()
