from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequire

engine = create_engine(db_string)
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

class Course():
    def newCourse():
        try:
            #new student
            newItem= Course(name=request.form['name'], lesson=request.form['lesson'])
            session.add(newItem)
            session.commit()
            flash("New student added")


       except Exception as e:
            return e
