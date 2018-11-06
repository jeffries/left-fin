from contextlib import contextmanager
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import nemo.config

logger = logging.getLogger(__name__)

Base = declarative_base()

engine = create_engine(nemo.config.DB_STRING, echo=True)
Session = scoped_session(sessionmaker(bind=engine))

def init():
    logger.info('standing tables')
    Base.metadata.create_all(engine)

# Provides a transactional scope
@contextmanager
def session_scope():
    s = Session()
    
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()
