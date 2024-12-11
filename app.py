from models import db, User

# run our app

# Create
user = User(first_name="Ken", email="ken@gmail.com",phone="0712345678")

# add the use instance the db transaction
# db.add(user)
# commit the transaction
# db.commit()

# Read
users = db.query(User).all()

print(users)
