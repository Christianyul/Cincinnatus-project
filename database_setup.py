from dependencies import *
from user import *
from course import *
from student import *
from medicalData import *
from schedule import *

#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()


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
except Exception as e:
    pass

#instance or create engine class
#///----cambiar password------///
db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)

#this will add the classes that we will create as tables in our database
Base.metadata.create_all(engine)

print "database setup done"
