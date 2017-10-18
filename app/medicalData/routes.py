from flask import Flask, render_template, url_for
from . import MedicalRouting
from database_setup import *
from medicalForm import MedicalForm
from flask import Blueprint, jsonify
import os

methods = ['GET', 'POST']
GET, POST = methods

nl = "\n"

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)


@MedicalRouting.route("/<int:student_id>/medical/medicalapi")
def MedicalApi(student_id):
    Info = []
    student = session.query(Student).filter_by(id=student_id)
    medical = session.query(MedicalData).filter_by(id =student_id).all()
    for data in medical:
        Data = {}
        Data["id"] = data.id
        Data["Student_Id"] = data.student
        Data["alergies_of_the_student"] = data.alergies
        Data["Intensity_of_the_alergies"] = data.intensity
        Data["Special_Condition"] = data.special_condition
        Data["Blood_Type"] = data.blood_type
        Data["Ars"] = data.ars
        Data["Afliation_type"] = data.afiliation_type
        Data["policy_number"] = data.policy_number
        Info.append(Data)
    MedicalDataApi = {"All_Data": Info}
    return jsonify(MedicalDataApi)

@MedicalRouting.route("/<int:student_id>/medical/")
def showMedical(student_id):
    student=session.query(Student).filter_by(id=student_id).one()
    item=session.query(MedicalData).filter_by(student=student_id).all()
    print item
    return render_template("medical.html", item=item, student = student )


@MedicalRouting.route("/<int:student_id>/medical/register/", methods=['GET','POST'])
def newMedical(student_id):
    form = MedicalForm()
    student=session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():
        # si no hay nada en policy_number se agrega 0 por default
        if len(request.form['policy_number'])> 0:
            policy_num=request.form['policy_number']
        else:
            policy_num = 0


        # si no hay nada en alergies se agrega "Ninguna" por default
        if len(request.form['alergies']) > 0:
            aler = request.form['alergies']
        else:
            aler = "Ninguna"      


        if len(request.form['special_condition']) > 0:
            special = request.form['special_condition']
        else:
            special = "Ninguna"       
        

        newItem=MedicalData(
        alergies=aler,
        intensity=request.form['intensity'],
        special_condition=special,
        blood_type=request.form['blood_type'],
        ars=request.form['ars'],
        afiliation_type=request.form['afiliation_type'],
        policy_number = policy_num,
        student=student.id)

        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        # return redirect(url_for('MedicalRouting.showMedical',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("medicalsignup.html", form=form, student=student)




@MedicalRouting.route("/<int:student_id>/medical/<int:medical_id>/edit/", methods=['GET','POST'])
def editMedical(medical_id,student_id):
    form = MedicalForm()
    student=session.query(Student).filter_by(id=student_id).one()
    editedItem = session.query(MedicalData).filter_by(id=medical_id).one()
    if form.validate_on_submit():

        # si no hay nada en policy_number se agrega 0 por default
        if len(request.form['policy_number'])> 0:
            policy_num=request.form['policy_number']
        else:
            policy_num = 0

        editedItem.alergies=request.form['alergies']
        editedItem.intensity=request.form['intensity']
        editedItem.special_condition=request.form['special_condition']
        editedItem.blood_type=request.form['blood_type']
        editedItem.ars=request.form['ars']
        editedItem.afiliation_type=request.form['afiliation_type']
        editedItem.policy_number = policy_num
        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        # return redirect(url_for('MedicalRouting.showMedical',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("editmedical.html",form=form, medical_id=medical_id, item=editedItem, student=student)



@MedicalRouting.route("/<int:student_id>/medical/<int:medical_id>/delete/", methods=['GET','POST'])
def deleteMedical(medical_id, student_id):
    student=session.query(Student).filter_by(id=student_id).one()
    if request.method == 'POST':
        deletedItem = session.query(MedicalData).filter_by(id=medical_id).one()
        session.delete(deletedItem)
        session.commit()
        # return redirect(url_for('MedicalRouting.showMedical',student_id=student.id))
        return redirect(url_for('StudentRouting.showStudent'))

    return render_template("deletemedical.html",medical_id=medical_id, student=student)
