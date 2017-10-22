from flask import Flask, render_template, url_for, request, jsonify, redirect
from . import StudentRouting
from database_setup import *
from studentForm import StudentForm
from flask import Blueprint
import os
from werkzeug.utils import secure_filename

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app\static\images")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Student_API():
    StudentItem=session.query(Student).all()
    Data = {}
    for data in StudentItem:  
        Data['id'] = str(data.id)
        Data['name'] = str(data.name)
        Data['last_name'] = str(data.last_name)
        Data['email'] = str(data.email)
        Data['image_path'] = str(data.image_path)
        Data['gender'] = str(data.gender)
        Data['incription_date'] = str(data.inscription_date)
        Data['birthdate'] = str(data.birthdate)
        Data['phone_mobile'] = str(data.phone_mobile)
        Data['id_document'] = str(data.id_document)
        Data['status'] = str(data.status)
        Data['ending_date'] = str(data.ending_date)
        Data['retirement_date'] = str(data.retirement_date)
        Data['actual_course'] = str(data.actual_course)
        Data['actual_lesson'] = str(data.marital_status)
        Data['nationality'] = str(data.nationality)
        Data['address'] = str(data.address)
    return jsonify(Data) 


@StudentRouting.route("/student/",  methods=['GET','POST'])
def showStudent():
    print Student_API()
    item=session.query(Student).all()
    if request.method == 'POST':
        searchText= request.form["search"]
        student=session.query(Student).filter(Student.id_document.like(searchText+"%")).all()
        print student
        return render_template("student.html", item=student)
    else:   
        print item
        return render_template("student.html", item=item)

@StudentRouting.route("/student/register/", methods=['GET','POST'])
def newStudent():
    form = StudentForm()
    courses=session.query(Course).all()
    if form.validate_on_submit():
        
        re_date=request.form['retirement_date']
        end_date=request.form['ending_date']

        if len(re_date) <= 0:
            re_date = "0001-01-01"

        if len(end_date) <=0:
            end_date = "0001-01-01"

        if 'file' not in request.files or request.files['file'].filename == '':
            filename = "default.jpg"
        else:
            file = request.files['file']
        # if user does not select file, browser also submit a empty part without filename
        # if not os.path.isdir(UPLOAD_FOLDER):
        #     os.mkdir(UPLOAD_FOLDER)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                filename = "default.jpg"

        print filename

        print form.errors
        print "its happening 2"
        newItem=Student(name=request.form['name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        gender=request.form['gender'],
        image_path=filename,
        inscription_date=request.form['inscription_date'],
        ending_date=end_date,
        retirement_date=re_date,
        birthdate=request.form['birthdate'],
        phone_mobile=request.form['phone_mobile'],
        phone_home=request.form['phone_home'],
        actual_course=request.form['actual_course'],
        id_document=request.form['id_document'],
        status=request.form['status'],
        marital_status=request.form['marital_status'],
        nationality=request.form['nationality'],
        address=request.form['address'])

        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))

    print "its happening 1"

    return render_template("studentsignup.html", form=form, courses=courses)


@StudentRouting.route("/student/<int:student_id>/edit/", methods=['GET','POST'])
def editStudent(student_id):
    form = StudentForm()
    courses=session.query(Course).all()
       
    editedItem = session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():

        print APP_ROOT
        print UPLOAD_FOLDER
    
        re_date=request.form['retirement_date']
        end_date=request.form['ending_date']

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
        editedItem.last_name=request.form['last_name']
        editedItem.email=request.form['email']
        if filename:
            editedItem.image_path=filename
        editedItem.gender=request.form['gender']
        editedItem.inscription_date=request.form['inscription_date']
        editedItem.ending_date=end_date
        editedItem.retirement_date=re_date
        editedItem.birthdate=request.form['birthdate']
        editedItem.phone_mobile=request.form['phone_mobile']
        editedItem.phone_home=request.form['phone_home']
        editedItem.actual_course=request.form['actual_course']
        editedItem.id_document=request.form['id_document']
        editedItem.status=request.form['status']
        editedItem.marital_status=request.form['marital_status']
        editedItem.nationality=request.form['nationality']
        editedItem.address=request.form['address']
        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("editstudent.html",form=form, student_id=student_id, item=editedItem, courses=courses)



@StudentRouting.route("/student/<int:student_id>/delete/", methods=['GET','POST'])
def deleteStudent(student_id):
    if request.method == 'POST':
        deletedItem = session.query(Student).filter_by(id=student_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('StudentRouting.showStudent'))

    return render_template("deletestudent.html",student_id=student_id)