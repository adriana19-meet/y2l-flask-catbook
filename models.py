from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cat(Base):
    __tablename__ = "cats"
    id = Column(Integer, primary_key=True)
<<<<<<< HEAD
    name = Column(String)
    image = Column(String)
    votes = Column(Integer)
    
=======
    name = Column(String)
>>>>>>> 99f6c5c5474db4767939c4d93959e4a68fcce36f
