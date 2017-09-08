from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import *

app=Flask(__name__)
db_string="postgres://postgres:0321help@localhost:5432/cincinnatus"
engine = create_engine(db_string)
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

@app.route("/")
def Welcome():
    items=session.query(Student).all()
    return jsonify(Student=[i.serialize for i in items])

if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
