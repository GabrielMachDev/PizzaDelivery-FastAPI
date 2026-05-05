from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# create database connection
db = create_engine("sqlite:///bank.db")

# create base for database
Base = declarative_base()

# create an class/table for database
class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    email = Column("email", String, nullable = False)
    password = Column("password", String)
    status = Column("status", Boolean)
    admin = Column("admin", Boolean, default = False)

    def __init__(self, name, email, password, status = True, admin = False):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.admin = admin

class Order(Base):
    __tablename__ = "orders"

    # ORDER_STATUS = {
    #     ("PENDING", "PENDING"),
    #     ("CANCELED", "CANCELED"),
    #     ("FINISH", "FINISH")
    # }

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    user = Column("user", ForeignKey("users.id"))
    status = Column("status", String)
    price = Column("price", Float)

    def __init__(self, user, status="PENDING", price = 0):
        self.user = user
        self.status = status
        self.price = price

class OrderItem(Base):
    __tablename__ = "orderItems"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unitPrice = Column("unitPrice", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, flavor, size, unitPrice, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unitPrice = unitPrice
        self.order = order