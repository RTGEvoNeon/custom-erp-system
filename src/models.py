from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Sort(Base):
    __tablename__ = "sorts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)
    planted = Column(Integer, default=0)
    harvested = Column(Integer, default=0)
    sold = Column(Integer, default=0)
    died = Column(Integer, default=0)
    shade_id = Column(Integer, ForeignKey("shades.id"))
    image_id = Column(Integer, ForeignKey("images.id"))

    # Связывание с внешней таблицей в sqlalchemy
    shade = relationship("Shade", back_populates="sorts")
    image = relationship("Image", back_populates="sorts")


class Shade(Base):
    __tablename__ = "shades"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)

    # Связывание с внешней таблицей в sqlalchemy
    sorts = relationship("Sort", back_populates="shade")


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, unique=True, nullable=False)
    url = Column(String, unique=True, nullable=False)

    # Связывание с внешней таблицей в sqlalchemy
    sorts = relationship("Sort", back_populates="image")


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    full_price = Column(Integer, default=0)
    prepayment = Column(Integer, default=0)
    datetime = Column(DateTime, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))
    state_id = Column(Integer, ForeignKey("states.id"))

    # Связывание с внешней таблицей в sqlalchemy
    client = relationship("Client", back_populates="orders")
    state = relationship("State", back_populates="orders")


class State(Base):
    __tablename__ = "states"
    title = Column(String, unique=True, nullable=False)

    # Связывание с внешней таблицей в sqlalchemy
    order = relationship("Order", back_populates="state")


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    patronymic = Column(String)
    phone_number = Column(String, nullable=False)

    # Связывание с внешней таблицей в sqlalchemy
    orders = relationship("Order", back_populates="client")
    order_positions = relationship("OrderPosition", back_populates="client")


class OrderPosition(Base):
    __tablename__ = "order_positions"
    id = Column(Integer, primary_key=True, index=True)
    number_of_flower = Column(Integer, nullable=False)
    sort_id = Column(Integer, ForeignKey("sorts.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))

    # Связывание с внешней таблицей в sqlalchemy
    sort = relationship("Sort", back_populates="order_positions")
    client = relationship("Client", back_populates="order_positions")





