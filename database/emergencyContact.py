from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database

class EmergencyContact(Base):
    __tablename__="emergency_contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_mobile = Column(String(12), nullable=False)
    phone_home = Column(String(12))
    relationship = Column(String(20), nullable=False)
    student = Column(Integer, ForeignKey('students.id'))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'phone_mobile': self.phone_mobile,
        'phone_home': self.phone_home,
        'relationship': self.relationship,
        'student': self.student,
        }
