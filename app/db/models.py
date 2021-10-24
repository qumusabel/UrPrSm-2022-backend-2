# pyright: reportGeneralTypeIssues=false
from datetime import datetime

from ..server import db

Model = db.Model
Column = db.Column
ForeignKey = db.ForeignKey
relationship = db.relationship

Integer, Text, Float, Date= db.Integer, db.Text, db.Float, db.Date

column = lambda *args, **kwargs: Column(*args, **kwargs, nullable=False)
str_date = lambda: datetime.utcnow().date()


class Bouquet(Model):
    __tablename__ = "bouquet"

    id = Column(Integer, primary_key=True)
    name = column(Text)
    price = column(Float)
    photoUrl = column(Text)

    sellerId = column(Integer, ForeignKey("seller.id"))
    seller = relationship("Seller", back_populates="bouquets")


class Seller(Model):
    __tablename__ = "seller"

    id = Column(Integer, primary_key=True)
    name = column(Text)
    photoUrl = column(Text)
    dateCreated = column(Date, default=str_date)

    bouquets = relationship("Bouquet", back_populates="seller")

    bouquetsSold = column(Integer, default=0)


class Customer(Model):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = column(Text)
    email = column(Text)

    purchases = relationship("Purchase", back_populates="customer")


class Purchase(Model):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True)

    bouquetId = column(Integer, ForeignKey("bouquet.id"))
    bouquet = relationship("Bouquet")

    customerId = column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer", back_populates="purchases")

    price = column(Float)
    commission = column(Float)

