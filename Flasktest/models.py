from sqlalchemy import Column, Integer, String
from Flasktest.database import Base

class Entry(Base):
  __tablename__ = 'entry'
  id = Column(Integer, primary_key=True)
  firstname = Column(String(30), unique=False)
  lastname = Column(String(30), unique=False)
  email = Column(String(40), unique=True)
  address = Column(String(80), unique=False)

  def __init__(self, firstname=None, lastname=None, email=None, address=None):
    self.firstname = firstname
    self.lastname = lastname
    self.email = email
    self.address = address

  def __repr__(self):
    '<Entry %r>' % (self.firstname)



#id = Column(Integer, primary_key=True)
 # title = Column(String(20), unique=False)
  #text = Column(String(200), unique=False)

#  def __init__(self, title=None, text=None):
	#self.title = title
	#self.text = text

#  def __repr__(self):
	#'<Entry %r>' % (self.title)

#class User(Base):
#  __tablename__ = 'user'
  
