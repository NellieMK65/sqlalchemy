from models import db, User, Account
from sqlalchemy.orm import joinedload
# run our app

# Create
user = User(first_name="Ken", email="ken@gmail.com",phone="0712345678")

# add the use instance the db transaction
# db.add(user)
# commit the transaction
# db.commit()

account = Account(user_id = 1, working_balance=100, balance=500, credit_score=200)

# db.add(account)
# db.commit()

# Read
# retrieve all records from the table
# users = db.query(User).all()

# print(users)

# retrieve a single record using a specific column
user = db.query(User).options(joinedload(User.accounts)).filter(User.id == 1).first()

print(user)

# Updating
# 1. Retrieve the record
# user2 = db.query(User).filter(User.id == 1).first()

# update the necessary fields
# user2.phone = '0712345678'

# db.add(user2)
# db.commit()


# Deleting

# 1. Select the record
# user3 = db.query(User).filter(User.id == 2).first()

# 2. run the delete method
# db.delete(user3)

# 3. commit transaction
# db.commit()
