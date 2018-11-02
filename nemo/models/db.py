from contextlib import contextmanager
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

logger = logging.getLogger(__name__)

engine = create_engine('postgres://nemo:nemo@db/nemo', echo=True)

Session = sessionmaker()
Session.configure(bind=engine)

Base = declarative_base()

def init():
    logger.info('standing tables')
    Base.metadata.create_all(engine)

# Provides a convenient transaction context
# with transaction() as t:
#     pass
@contextmanager
def transaction():
    s = Session()
    yield s
    s.commit()
