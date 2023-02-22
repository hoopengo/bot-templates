from type import Optional
from datetime import datetime

from mymodule.base import Base
from sqlalchemy import Column, DateTime, Integer


class Ban(Base):
    __tablename__ = "ban"
    __slots__ = ('id', 'user_id', 'expired')

    id: int = Column(Integer, primary_key=True, index=True)
    user_id: int = Column(Integer, nullable=False)
    expired: Optional[datetime] = Column(DateTime, nullable=True, default=None)

    def __repr__(self) -> str:
        return f"ID: {self.user_id}, Expired: {self.expired or 'no.'}"


def sync(base, engine):
    base.metadata.create_all(engine)
