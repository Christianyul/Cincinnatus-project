from flask import Flask, render_template, url_for
from . import RegisterRouting
from database_setup import *
from registerForm import RegisterForm
from flask import Blueprint
import os

methods = ['GET', 'POST']
GET, POST = methods

nl = "\n"

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)



@RegisterRouting.route("/", methods=['GET','POST'])
def register():
    return "hello"


@RegisterRouting.route("/register/", methods=['GET','POST'])
def registerStudent():
    form=RegisterForm()

    if form.validate_on_submit():
        # filename = secure_filename(request.form['image_path'])
        # print os.path.realpath(filename)
        # file.save(os.path.join('/static/Pictures', filename))
        print form.errors
        print "its happening 2"
        newStudent=Student(name=request.form['name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        gender=request.form['gender'],
        inscription_date=request.form['inscription_date'],
        ending_date=request.form['ending_date'],
        retirement_date=request.form['retirement_date'],
        birthdate=request.form['birthdate'],
        phone_mobile=request.form['phone_mobile'],
        phone_home=request.form['phone_home'],
        id_document=request.form['id_document'],
        status=request.form['status'],
        marital_status=request.form['marital_status'],
        nationality=request.form['nationality'],
        address=request.form['address'])
            # os.path.realpath(filename)

        session.add(newStudent)
        session.flush()

        if len(request.form['policy_number'])> 0:
            policy_num=request.form['policy_number']
        else:
            policy_num = 0

        newMedical=MedicalData(
        alergies=request.form['alergies'],
        intensity=request.form['intensity'],
        special_condition=request.form['special_condition'],
        blood_type=request.form['blood_type'],
        ars=request.form['ars'],
        afiliation_type=request.form['afiliation_type'],
        policy_number = policy_num,
        student=newStudent.id)

        session.add(newMedical)

        newEmergency=EmergencyContact(name=request.form['emname'],
        last_name=request.form['emlast_name'],
        phone_mobile=request.form['emphone_mobile'],
        phone_home=request.form['emphone_home'],
        relationship=request.form['relationship'],
        student=newStudent.id)

        session.add(newEmergency)

        session.commit()
    return render_template("register.html", form=form)
