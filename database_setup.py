from dependencies import *
from database import *


#instances of the clases/tables
# us= User()
# co= Course()
# st= Student()
# me= MedicalData()
# sc= Schedule()
# em= EmergencyContact()


#create database
#////----cambiar password-------///
#if database is created we control the exception by simply passing
try:
    connect = connect(user = 'postgres', host='localhost', port= '5001', password='linkinpark09', dbname= 'cincinnatus')
except:
    try:
        con = connect(user='postgres', host = 'localhost', port='5001', password='linkinpark09')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur= con.cursor()
        cur.execute('CREATE DATABASE' + "cincinnatus")
        cur.close()
        con.close()

        us= User()
        co= Course()
        st= Student()
        me= MedicalData()
        sc= Schedule()
        em= EmergencyContact()

        #///----cambiar password------///
        db_string="postgres://postgres:linkinpark09@localhost:5001/cincinnatus"
        engine = create_engine(db_string)
        #this will add the classes that we will create as tables in our database
        Base.metadata.create_all(engine)

        # DBSession=sessionmaker(bind=engine)
        # session=DBSession()
        print "database setup done"
    except Exception as e:
        print e 

