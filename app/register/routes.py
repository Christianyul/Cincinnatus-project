from flask import Flask, render_template, url_for, request
from . import RegisterRouting
from database_setup import *
from registerForm import RegisterForm
from flask import Blueprint
import os
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app/static/images")
 

print UPLOAD_FOLDER
db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@RegisterRouting.route("/", methods=['GET','POST'])
def register():
    return "hello"

@RegisterRouting.route("/register/", methods=['GET','POST'])
def registerStudent():
    form=RegisterForm()
    courses=session.query(Course).all()
    print APP_ROOT
    print UPLOAD_FOLDER
    if form.validate_on_submit():

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
        

        print form.errors
        print "its happening 2"
        newStudent=Student(name=request.form['name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        image_path=filename,
        gender=request.form['gender'],
        inscription_date=request.form['inscription_date'],
        birthdate=request.form['birthdate'],
        phone_mobile=request.form['phone_mobile'],
        phone_home=request.form['phone_home'],
        actual_course=request.form['actual_course'],
        id_document=request.form['id_document'],
        status=request.form['status'],
        marital_status=request.form['marital_status'],
        nationality=request.form['nationality'],
        address=request.form['address'])
    

        session.add(newStudent)
        session.flush()


        if len(request.form['policy_number'])> 0:
            policy_num = request.form['policy_number']
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


        newMedical=MedicalData(
        alergies=aler,
        intensity=request.form['intensity'],
        special_condition=special,
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
    return render_template("register.html", form=form, courses=courses)
