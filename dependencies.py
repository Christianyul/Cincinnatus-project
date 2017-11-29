from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
#---------Cambiar password----------#
Base = declarative_base()
user="postgres"
password="011741"
server="localhost"
port="5432"
dbname="cincinnatus"
db_string="postgres://%s:%s@%s:%s/%s" % (user, password, server, port, dbname)
# db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
