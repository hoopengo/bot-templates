from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

engine = create_engine("sqlite:///db.sqlite3", echo=True)

Base = declarative_base()


@contextmanager
def session(**kwargs):
    new_session: Session = sessionmaker(
        engine,
        autocommit=False,
        autoflush=False,
        **kwargs,
    )
    try:
        yield new_session
    except Exception:
        new_session.rollback()
        raise
    else:
        new_session.commit()
    finally:
        new_session.close()
