from database import *
from dependencies import *

#create database
try:
    connect = connect(user = user, host= server, port = port, password = password, dbname = dbname)
except Exception as e:
    print "Creating Database..."
    try:
        con = connect(user = user, host= server, port = port, password = password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur= con.cursor()
        cur.execute('CREATE DATABASE' + " cincinnatus")
        cur.close()
        con.close()

        us= User()
        co= Course()
        st= Student()
        me= MedicalData()
        sc= Schedule()
        em= EmergencyContact()
        #///----cambiar password------///
        engine = create_engine(db_string)
        #this will add the classes that we will create as tables in our database
        Base.metadata.create_all(engine)

        print "Database Setup Done"
    except Exception as e:
         print e
