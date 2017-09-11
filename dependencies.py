from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy import Column,Date,Integer, ForeignKey, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, load_only
from sqlalchemy import create_engine
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#instance or declarative class
#this will let sqlalchemy know that our classes are special classses
#that correspond to tables in our database
Base = declarative_base()
