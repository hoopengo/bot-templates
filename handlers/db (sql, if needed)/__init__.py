from db.base import Base, engine, session
from db.models import sync

sync(Base, engine)
