from db.base import Base
from sqlalchemy import Column, DateTime, Integer


class Ban(Base):
    __tablename__ = "ban"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    expired = Column(DateTime, nullable=True)

    __mapper_args__ = {"eager_defaults": True}

    def __repr__(self) -> str:
        return f"ID: {self.user_id}, Expired: {self.expired or 'no.'}"


def sync(base, engine):
    base.metadata.create_all(engine)
