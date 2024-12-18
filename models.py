# define our tables using OOP + sqlalchemy
from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Text, Integer, VARCHAR, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship


# connect to the the db using sessionmaker (similar to sqlite conn)
engine = create_engine('sqlite:///app.db', echo=True)

# create a session
Session = sessionmaker(bind=engine)

db = Session()

# create a base model that all our models are going to inherit from
Base = declarative_base()

# define model
"""
1. Its a must we provide the table name via the attribute __tablename__
2. It`s must we provide at least one table column
"""
class User(Base):
    __tablename__ = "users"

    # define columns
    id = Column(Integer(), primary_key=True)
    first_name = Column(Text(), nullable=False) # NOT NULL
    email = Column(VARCHAR(), nullable=False, unique=True) # NOT NULL, UNIQUE
    phone = Column(Integer(), nullable=True) # NOT NULL, UNIQUE

    # one to many
    accounts = relationship("Account", backref="user")

    def __repr__(self):
        accounts_lenght = len(self.accounts)
        return f"(User {self.id}: Firstname: {self.first_name}, Email: {self.email}, Phone: {self.phone}, Accounts: {self.accounts} )"

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer(), primary_key=True)
    working_balance = Column(Integer())
    balance = Column(Integer())
    credit_score= Column(Integer())
    user_id= Column(Integer(), ForeignKey('users.id'))

    # many to one
    # user = relationship("User", backref="acccounts", uselist=False)

    # timestamp
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime())

    def __repr__(self) -> str:
        return f"(Account {self.id}: Balance: {self.balance})"
