"""Module for interacting with backend database"""

from contextlib import contextmanager
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import nemo.config

LOGGER = logging.getLogger(__name__)

BASE = declarative_base()

ENGINE = create_engine(nemo.config.DB_STRING, echo=True)
SESSION = scoped_session(sessionmaker(bind=ENGINE))

def init():
    """Initializes database by creating tables"""

    LOGGER.info('standing tables')
    BASE.metadata.create_all(ENGINE)

# Provides a transactional scope
@contextmanager
def session_scope():
    """Provides a session tied to the current request scope"""

    session = SESSION()

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
