from .base import Base, engine
from .models import sync

sync(Base, engine)
