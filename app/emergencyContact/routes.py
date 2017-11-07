from flask import Flask, render_template, url_for, jsonify, request, redirect
from . import EmergencyRouting
from database_setup import *
from emergencyForm import EmergencyForm
from flask import Blueprint
import os
from flask_login import login_required
from app import login_manager

@login_manager.user_loader
def user_loader(id):
    # do whatever you need to to load the user object
    # a database query, for example
    user= session.query(User).filter_by(id=id).one()
    return user

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

def phone_number_filtration(PhoneNumber):
    if PhoneNumber.isdigit():
        return int(PhoneNumber)
    else:
        newformat = PhoneNumber.replace("-", "", 2)
        if newformat.isdigit():
            return int(newformat)
        else:
            return 

@EmergencyRouting.route("/<int:student_id>/emergency/emergencyapi")
def EmergencyApi(student_id):
    Info = []
    student = session.query(Student).filter_by(id=student_id)
    emergency = session.query(EmergencyContact).filter_by(id =student_id).all()
    for data in emergency:
        Data = {}
        Data["id"] = data.id
        Data["Student_ID"] = data.student
        Data['last_name'] = data.last_name
        Data["Name_Emergency_Contact"] = data.name
        Data["Emergency_Phone_Mobile"] = data.phone_mobile
        Data["Emergency_Phone_Home"] = data.phone_home
        Data["Relationship_with_the_contact"] = data.relationship
        Info.append(Data)
    EmergencyData = {"All_Data": Info}
    return jsonify(EmergencyData)

@EmergencyRouting.route("/<int:student_id>/emergency/")
#@login_required
def showEmergency(student_id):
    student=session.query(Student).filter_by(id=student_id).one()
    item=session.query(EmergencyContact).filter_by(student=student_id).all()
    return render_template("emergency.html", item=item, student = student )


@EmergencyRouting.route("/<int:student_id>/emergency/register/", methods=['GET','POST'])
#@login_required
def newEmergency(student_id):
    form = EmergencyForm()
    student=session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():
        newItem = EmergencyContact(name = request.form['name'],
        last_name = request.form['last_name'],
        phone_mobile = phone_number_filtration(request.form['phone_mobile']),
        phone_home = phone_number_filtration(request.form['phone_home']),
        relationship = request.form['relationship'],
        student = student.id)

        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        # return redirect(url_for('EmergencyRouting.showEmergency',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("emergencysignup.html", form=form, student=student)




@EmergencyRouting.route("/<int:student_id>/emergency/<int:emergency_id>/edit/", methods=['GET','POST'])
# @login_required
def editEmergency(emergency_id,student_id):
    form = EmergencyForm()
    student=session.query(Student).filter_by(id=student_id).one()
    editedItem = session.query(EmergencyContact).filter_by(id=emergency_id).one()
    if form.validate_on_submit():
        editedItem.name = request.form['name']
        editedItem.last_name=request.form['last_name']
        editedItem.phone_mobile=request.form['phone_mobile']
        editedItem.phone_home=request.form['phone_home']
        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        # return redirect(url_for('EmergencyRouting.showEmergency',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("editemergency.html",form=form, emergency_id=emergency_id, item=editedItem, student=student)



@EmergencyRouting.route("/<int:student_id>/emergency/<int:emergency_id>/delete/", methods=['GET','POST'])
@login_required
def deleteEmergency(emergency_id, student_id):
    student=session.query(Student).filter_by(id=student_id).one()
    if request.method == 'POST':
        deletedItem = session.query(EmergencyContact).filter_by(id=emergency_id).one()
        session.delete(deletedItem)
        session.commit()
        # return redirect(url_for('EmergencyRouting.showEmergency',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))

    return render_template("deleteemergency.html",emergency_id=emergency_id, student=student)
