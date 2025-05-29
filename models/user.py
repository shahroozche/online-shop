from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db

class User(db.Model):
    __tablename__= "users"
    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    username:Mapped[str] = mapped_column(unique=True,nullable=False,index=True)
    password: Mapped[str] = mapped_column(nullable=False,index=True)
    phone: Mapped[str] = mapped_column(String(11),unique=True,index=True)
    address: Mapped[str]= mapped_column(nullable=False,index=True)