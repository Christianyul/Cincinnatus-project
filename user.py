from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    name = Column(String(50), nullable=False)
    user_name = Column(String(50), primary_key=True)
    password = Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    user_type= Column(String(50), nullable=False)
    student = Column(Integer, ForeignKey('students.id'))
