from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(20))  # Add phone number field
    birthday = Column(Date)  # Add birthday field
    additional_data = Column(String(255))  # Add optional additional data field
    created_at = Column('created_at', DateTime, default=func.now())
