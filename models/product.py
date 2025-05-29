from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

class Product(db.Model):
    __tablename__= "products"
    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name:Mapped[str] = mapped_column(unique=True,nullable=False,index=True)
    description: Mapped[str]= mapped_column(nullable=False,index=True)
    price: Mapped[int] = mapped_column(nullable=False,index=True)