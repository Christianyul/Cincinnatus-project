from dependencies import *
from user import *
from course import *
from student import *
from medicalData import *
from schedule import *
from emergencyContact import *

#instances of the clases/tables
us= User()
co= Course()
st= Student()
me= MedicalData()
sc= Schedule()
em= EmergencyContact()


#create database
#////----cambiar password-------///
#if database is created we control the exception by simply passing
try:
    con = connect(user='postgres', host = 'localhost', password='011741')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur= con.cursor()
    cur.execute('CREATE DATABASE' + " cincinnatus")
    cur.close()
    con.close()

    #///----cambiar password------///
    db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
    engine = create_engine(db_string)

    #this will add the classes that we will create as tables in our database
    Base.metadata.create_all(engine)

    DBSession=sessionmaker(bind=engine)
    session=DBSession()


    session.add(co)
    session.add(st)
    session.add(me)
    session.add(us)
    session.add(sc)
    session.add(em)
    session.commit()



except Exception as e:
    pass


print "database setup done"
