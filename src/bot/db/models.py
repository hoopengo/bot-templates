from sqlalchemy import BigInteger, Column, Integer

from bot.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    discord_id = Column(BigInteger, unique=True)

    def __init__(self, name, discord_id):
        self.name = name
        self.discord_id = discord_id

    def __repr__(self):
        return f"<User {self.discord_id}>"
