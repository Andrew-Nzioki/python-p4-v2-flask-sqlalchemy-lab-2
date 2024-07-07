from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Customer(db.Model):
    __tablename__ = 'customers'

    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(db.String)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id:Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name:Mapped[str] = mapped_column(db.String)
    price:Mapped[float] = mapped_column(db.Float)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'
