from flask import Flask, render_template, url_for, request, jsonify, redirect
from . import StudentRouting
from database_setup import *
from studentForm import StudentForm
from flask import Blueprint
import os
from werkzeug.utils import secure_filename
from flask_login import login_required
from app import login_manager

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

ALLOWED_EXTENSIONS = set(['svg', 'png', 'jpg', 'jpeg', 'gif'])
APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app\static\images")

@login_manager.user_loader
def user_loader(id):
    # do whatever you need to to load the user object
    # a database query, for example
    user= session.query(User).filter_by(id=id).one()
    return user

def allowed_file(filename):
    if filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

def phone_number_filtration(PhoneNumber):
    if PhoneNumber.isdigit():
        return int(PhoneNumber)
    else:
        newformat = PhoneNumber.replace("-", "", 2)
        if newformat.isdigit():
            return int(newformat)
        else:
            return 
    
def Student_API(data):
    Data = {}  
    Data['id'] = str(data.id)
    Data['name'] = str(data.name)
    Data['last_name'] = str(data.last_name)
    Data['email'] = str(data.email)
    Data['image_path'] = str(data.image_path)
    Data['gender'] = str(data.gender)
    Data['incription_date'] = str(data.inscription_date)
    Data['birthdate'] = str(data.birthdate)
    Data['phone_mobile'] = str(data.phone_mobile)
    Data['phone_home'] = str(data.phone_home)
    Data['id_document'] = str(data.id_document)
    Data['status'] = str(data.status)
    Data['ending_date'] = str(data.ending_date)
    Data['retirement_date'] = str(data.retirement_date)
    Data['actual_course'] = str(data.actual_course)
    Data['actual_lesson'] = str(data.marital_status)
    Data['nationality'] = str(data.nationality)
    Data['address'] = str(data.address) 
    return Data

@StudentRouting.route("/student/studentapi/")
def Make_StudentApi():
    Students = session.query(Student).all()
    ArrayStudents = []
    AllData = {"All_Data": ArrayStudents}

    for student in Students:
        ArrayStudents.append(Student_API(student))

    return jsonify(AllData)


@StudentRouting.route("/student/",  methods=['GET','POST'])
@login_required
def showStudent():
    Students = session.query(Student).all()
    courses = session.query(Course).all()
    if request.method == 'POST':
        
        searchText = request.form["search"]
        student = session.query(Student).filter(Student.id_document.like(searchText+"%")).all()
        return render_template("student.html", item = student, course=courses)

    else:   
        return render_template("student.html", item = Students, course=courses)

@StudentRouting.route("/student/<int:student_id>/info/", methods=['GET','POST'])
@login_required
def infoStudent(student_id):
    student = session.query(Student).filter_by(id=student_id).one()
    medical_data=session.query(MedicalData).filter_by(student=student_id).all()
    contacts=session.query(EmergencyContact).filter_by(student=student_id).all()
    course=session.query(Course).filter_by(id=student.actual_course).one()
    return render_template("infostudent.html", student_id=student_id, student=student, medical=medical_data, contacts=contacts, course=course)


@StudentRouting.route("/student/register/", methods=['GET','POST'])
@login_required
def newStudent():
    form = StudentForm()
    courses=session.query(Course).all()
    if form.validate_on_submit():
        
        re_date=request.form['retirement_date']
        phonemobile = phone_number_filtration(request.form['phone_mobile'])
        phonehome = phone_number_filtration(request.form['phone_home'])
        end_date=request.form['ending_date']

        if len(re_date) <= 0:
            re_date = "0001-01-01"

        if len(end_date) <=0:
            end_date = "0001-01-01"

#----------------------IMAGE VALIDATION-------------------#
        if 'file' not in request.files or request.files['file'].filename == '':
            filename = "default.jpg"

        else:
            file = request.files['file']
        # if user does not select file, browser also submit a empty part without filename
        # if not os.path.isdir(UPLOAD_FOLDER):
        #     os.mkdir(UPLOAD_FOLDER)
            print allowed_file(file.filename)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                filename = "default.jpg"
#-----------------------PHONE VALIDATION--------------------------#
        if phonehome is None or phonemobile is None:
            return render_template("studentsignup.html", Error_Phone="One of the phone numbers is Invalid", form=form, courses=courses)
 

        newItem=Student(name=request.form['name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        gender = request.form['gender'],
        image_path = filename,
        inscription_date = request.form['inscription_date'],
        ending_date = end_date,
        retirement_date = re_date,
        birthdate = request.form['birthdate'],
        phone_mobile = phone_number_filtration(request.form['phone_mobile']),
        phone_home = phone_number_filtration(request.form['phone_home']),
        actual_course = request.form['actual_course'],
        id_document = request.form['id_document'],
        status = request.form['status'],
        marital_status = request.form['marital_status'],
        nationality = request.form['nationality'],
        address = request.form['address'])
        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))
    # print "its happening 1"
    return render_template("studentsignup.html", form=form, courses=courses)


@StudentRouting.route("/student/<int:student_id>/edit/", methods=['GET','POST'])
@login_required
def editStudent(student_id):
    form = StudentForm()
    courses = session.query(Course).all()
    editedItem = session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():
        # print APP_ROOT
        # print UPLOAD_FOLDER
        re_date = request.form['retirement_date']
        end_date = request.form['ending_date']
        if len(re_date) <= 0:
            re_date = "0001-01-01"
        if len(end_date) <=0:
            end_date = "0001-01-01"
        if 'file' not in request.files or request.files['file'].filename == '':
            filename= False
            pass
        else:
            file = request.files['file']
        # if not os.path.isdir(UPLOAD_FOLDER):
        #     os.mkdir(UPLOAD_FOLDER)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                filename = "default.jpg"

        editedItem.name = request.form['name']
        editedItem.last_name = request.form['last_name']
        editedItem.email = request.form['email']

        if filename:
            editedItem.image_path = filename

        editedItem.gender = request.form['gender']
        editedItem.inscription_date = request.form['inscription_date']
        editedItem.ending_date = end_date
        editedItem.retirement_date = re_date
        editedItem.birthdate = request.form['birthdate']
        editedItem.phone_mobile = phone_number_filtration(request.form['phone_mobile'])
        editedItem.phone_home = phone_number_filtration(request.form['phone_home'])
        editedItem.actual_course = request.form['actual_course']
        editedItem.id_document = request.form['id_document']
        editedItem.status = request.form['status']
        editedItem.marital_status = request.form['marital_status']
        editedItem.nationality = request.form['nationality']
        editedItem.address = request.form['address']
        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("editstudent.html",form=form, student_id=student_id, item=editedItem, courses=courses)


@StudentRouting.route("/student/<int:student_id>/delete/", methods=['GET','POST'])
@login_required
def deleteStudent(student_id):
    if request.method == 'POST':
        deletedItem = session.query(Student).filter_by(id=student_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('StudentRouting.showStudent'))

    return render_template("deletestudent.html",student_id=student_id)