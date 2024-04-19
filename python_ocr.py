'''
Recommended to use a virtual environment to install the required packages.
python -m venv python_ocr 
source python_ocr/bin/activate
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.base import Base
from models.user import User

# Create the database
engine = create_engine('sqlite:///python_ocr.db', echo=True)
Base.metadata.create_all(engine)

# Create a new session
session = Session(engine)

# Create new users
user1 = User(first_name="McLovin", last_name="NA")
user2 = User(first_name="Jordan", last_name="Keeley")

# Add the new users to the session
session.add(user1)
session.add(user2)

# Commit the session to write the changes to the database
session.commit()
