from flask import Flask, render_template, url_for, request, redirect
from . import RegisterRouting
from database_setup import *
from registerForm import RegisterForm
from loginForm import LoginForm
from flask import Blueprint
import os, hashlib
from werkzeug.utils import secure_filename
from flask_login import login_user
from flask_login import login_required
from app import login_manager

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app/static/images")

db_string="postgres://postgres:linkinpark09@localhost:5001/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
dbsession=DBSession()
app=Flask(__name__)

# try:
#     obj = str(obj).decode('utf8')
# except UnicodeEncodeError:
#     # already unicode
#     pass

def phone_number_filtration(PhoneNumber):
    if PhoneNumber.isdigit():
        return int(PhoneNumber)
    else:
        newformat = PhoneNumber.replace("-", "", 2)
        if newformat.isdigit():
            return int(newformat)
        else:
            return 
    

@login_manager.user_loader
def user_loader(id):
    # do whatever you need to to load the user object
    # a database query, for example
    user= dbsession.query(User).filter_by(id=id).one()
    return user

def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@RegisterRouting.route("/", methods=['GET','POST'])
def register():
    print hashlib
    return "hello"

@RegisterRouting.route("/login", methods=['GET','POST'])
def login():
    form=LoginForm()
    h = hashlib.md5() 
    if form.validate_on_submit():
       
        h.update(request.form['password'])
        user = dbsession.query(User).filter_by(user_name= request.form['user']).one()
        if user is not None and user.password == h.hexdigest():
            user.authenticated = True

            login_user(user)         
            return redirect(url_for('RegisterRouting.register'))
    return render_template('login.html', form=form)

@RegisterRouting.route("/register/", methods=['GET','POST'])
def registerStudent():
    form=RegisterForm()        
    courses=dbsession.query(Course).all()
    if form.validate_on_submit():
        phonemobile = phone_number_filtration(request.form['phone_mobile'])
        phonehome = phone_number_filtration(request.form['phone_home'])
        emergencyhome = phone_number_filtration(request.form['emphone_home'])
        emergencymobile = phone_number_filtration(request.form['emphone_mobile'])
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
        if phonemobile is None or phonehome is None or emergencyhome is None or emergencymobile is None:
            return render_template("register.html", courses=courses, form=form, errormsg="One of the phone numbers is Invalid")
        # print form.errors
        # print "its happening 2"
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
        dbsession.add(newStudent)
        dbsession.flush()
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
        dbsession.add(newMedical)

        newEmergency=EmergencyContact(name=request.form['emname'],
        last_name=request.form['emlast_name'],
        phone_mobile=request.form['emphone_mobile'],
        phone_home=request.form['emphone_home'],
        relationship=request.form['relationship'],
        student=newStudent.id)

        dbsession.add(newEmergency)
        dbsession.commit()
    return render_template("register.html", form=form, courses=courses)
