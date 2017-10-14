from flask import Flask, render_template, url_for, request
from . import StudentRouting
from database_setup import *
from studentForm import StudentForm
from flask import Blueprint
import os
from werkzeug.utils import secure_filename


db_string="postgres://postgres:linkinpark09@localhost:5001/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app\static\images")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Student_API(Student):
    Data = {}
    Data['id'] = str(Student.id)
    Data['name'] = str(Student.name)
    Data['last_name'] = str(Student.last_name)
    Data['email'] = str(Student.email)
    Data['image_path'] = str(Student.image_path)
    Data['gender'] = str(Student.gender)
    Data['incription_date'] = str(Student.inscription_date)
    Data['birthdate'] = str(Student.birthdate)
    Data['phone_mobile'] = str(Student.phone_mobile)
    Data['id_document'] = str(Student.id_document)
    Data['status'] = str(Student.status)
    Data['ending_date'] = str(Student.ending_date)
    Data['retirement_date'] = str(Student.retirement_date)
    Data['actual_course'] = str(Student.actual_course)
    Data['actual_lesson'] = str(Student.marital_status)
    Data['nationality'] = str(Student.nationality)
    Data['address'] = str(Student.address)
    return Data 

def Student_Data():
    Array_Data = []
    Api_Students = {"All the data": Array_Data}
    students = session.query(Student).all()
    for student in students:
        Array_Data.append(Student_API(student))
    return Api_Students

@StudentRouting.route("/student/")
def showStudent():
    item=session.query(Student).all()
    print Student_Data()
    return render_template("student.html", item=item)


@StudentRouting.route("/student/register/", methods=['GET','POST'])
def newStudent():
    form = StudentForm()
    if form.validate_on_submit():
        print APP_ROOT
        print UPLOAD_FOLDER
    
        re_date=request.form['retirement_date']
        end_date=request.form['ending_date']

        if 'file' not in request.files:
            flash('No image selected')
            print "No image selected"
            return redirect(request.url)

        file = request.files['file']
        # if user does not select file, browser also submit a empty part without filename
        if not os.path.isdir(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        if file.filename == '':
            flash('No image selected')
            print "No image selected"
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
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
        id_document=request.form['id_document'],
        status=request.form['status'],
        marital_status=request.form['marital_status'],
        nationality=request.form['nationality'],
        address=request.form['address'])
        # os.path.realpath(filename)


        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))


    print "its happening 1"

    return render_template("studentsignup.html", form=form)




@StudentRouting.route("/student/<int:student_id>/edit/", methods=['GET','POST'])
def editStudent(student_id):
    form = StudentForm()
       
    editedItem = session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():

        print APP_ROOT
        print UPLOAD_FOLDER
    
        re_date=request.form['retirement_date']
        end_date=request.form['ending_date']

        file = request.files['file']
        # if user does not select file, browser also submit a empty part without filename
        if not os.path.isdir(UPLOAD_FOLDER):
            os.mkdir(UPLOAD_FOLDER)

        if file.filename == '':
            flash('No selected file')
            print "No selected file"
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

        editedItem.name = request.form['name']
        editedItem.last_name=request.form['last_name']
        editedItem.email=request.form['email']
        editedItem.image_path=filename
        editedItem.gender=request.form['gender']
        editedItem.inscription_date=request.form['inscription_date']
        editedItem.ending_date=request.form['ending_date']
        editedItem.retirement_date=request.form['retirement_date']
        editedItem.birthdate=request.form['birthdate']
        editedItem.phone_mobile=request.form['phone_mobile']
        editedItem.phone_home=request.form['phone_home']
        editedItem.id_document=request.form['id_document']
        editedItem.status=request.form['status']
        editedItem.marital_status=request.form['marital_status']
        editedItem.nationality=request.form['nationality']
        editedItem.address=request.form['address']


        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("editstudent.html",form=form, student_id=student_id, item=editedItem)



@StudentRouting.route("/student/<int:student_id>/delete/", methods=['GET','POST'])
def deleteStudent(student_id):
    if request.method == 'POST':
        deletedItem = session.query(Student).filter_by(id=student_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('StudentRouting.showStudent'))

    return render_template("deletestudent.html",student_id=student_id)
