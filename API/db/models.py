from .database import Base
from sqlalchemy import Column, String, Integer

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))