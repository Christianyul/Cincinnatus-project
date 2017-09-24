from dependencies import *
#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database


class MedicalData(Base):
    __tablename__= "medical_data"
    id = Column(Integer, primary_key=True)
    alergies = Column(String(200))
    intensity = Column(String(20))
    special_condition = Column(String(50))
    blood_type = Column(String(50))
    ars = Column(String(20))
    afiliation_type = Column(String(20))
    policy_number = Column(Integer)
    student = Column(Integer, ForeignKey('students.id'))

    @property
    #returns an object data in easily serializeable format
    def serialize(self):
        return {
        'id': self.id,
        'alergies': self.alergies,
        'intensity': self.intensity,
        'special_condition': self.special_condition,
        'blood_type':self.blood_type,
        'ars': self.ars,
        'afiliation_type': self.afiliation_type,
        'policy_number': policy_number,
        'student': self.student,
        }
