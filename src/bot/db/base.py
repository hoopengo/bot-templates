import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import QueuePool

from bot.misc.config import config

engine = create_engine(config.POSTGRES_URL, echo=True, poolclass=QueuePool)
Base = declarative_base()
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

logger = logging.getLogger(__name__)


@contextmanager
def session(**kwargs):
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception as e:
        new_session.rollback()
        logger.error(f"Error in session: {e}")
        raise
    finally:
        new_session.close()
