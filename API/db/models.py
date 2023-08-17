from .database import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    items = relationship('DbPost', back_populates='user')

class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    image_url_type = Column(String(255))
    caption = Column(String(255))
    timestamp = Column(DateTime())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='items')