from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()

class Course(Base):
    __tablename__="courses"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    lesson = Column(Integer)
    link =Column(String(50))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'lesson': self.lesson,
        }
