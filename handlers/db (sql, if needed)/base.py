from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

engine = create_engine("sqlite:///db.sqlite3", echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@contextmanager
def session(**kwargs):
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except:
        new_session.rollback()
        raise
    finally:
        new_session.close()
