from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()

class Schedule(Base):
    __tablename__= "schedule"
    id = Column(Integer, primary_key=True)
    day = Column(String(200))
    daytime = Column(String(20))
    student = Column(Integer, ForeignKey('students.id'))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'day': self.day,
        'daytime':self.daytime,
        'student':self.student,
        }
