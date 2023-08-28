
from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from DB.database import Base, engine


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")



# def initialize_database():
#     Base.metadata.create_all(bind=engine)
#
#
# class User(Base):
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
#
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
#
#     owner = relationship("User", back_populates="items")
#
#
# class Place(Base):
#     __tablename__ = "places"
#
#     place_name = Column(String)
#     axis_x = Column(Float)
#     axis_y = Column(Float)
#     address = Column(String)
#     place_url = Column(String)
#     place_ID = Column(Integer, primary_key=True, index=True)
#     is_active = Column(Boolean, default=True)
#
#     items = relationship("Item", back_populates="owner")
