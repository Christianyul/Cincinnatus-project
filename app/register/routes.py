from flask import Flask, render_template, url_for, request, redirect, Blueprint
from . import RegisterRouting
from database_setup import sessionmaker, create_engine, db_string
from registerForm import RegisterForm
from loginForm import LoginForm
import os, hashlib
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user,  login_required
from app import login_manager

ALLOWED_EXTENSIONS = set(['svg' 'png', 'jpg', 'jpeg', 'gif'])

APP_ROOT= os.path.abspath(os.path.dirname(__name__))
UPLOAD_FOLDER = os.path.join(APP_ROOT,"app/static/images")

engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
dbsession=DBSession()
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
    
@login_manager.user_loader
def user_loader(id):
    # do whatever you need to to load the user object
    # a database query, for example
    user= dbsession.query(User).filter_by(id=id).one()
    return user

def allowed_file(filename):
    if filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    return False

@RegisterRouting.route("/", methods=['GET','POST'])
def register():
    students = dbsession.query(Student).all()
    courses = dbsession.query(Course).all()    
    return render_template("home.html", courses = courses, students = students)

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

@RegisterRouting.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('RegisterRouting.login'))


@RegisterRouting.route("/register/", methods=['GET','POST'])
def registerStudent():
    form=RegisterForm()        
    courses=dbsession.query(Course).all()

    if form.validate_on_submit():    
        idcourse=dbsession.query(Course).filter_by(id=request.form['actual_course']).one().id
        phonemobile = phone_number_filtration(request.form['phone_mobile'])
        phonehome = phone_number_filtration(request.form['phone_home'])
        emergencyhome = phone_number_filtration(request.form['emphone_home'])
        emergencymobile = phone_number_filtration(request.form['emphone_mobile'])

#-------------------------------IMAGE VALIDATION----------------------------------#
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

#-------------------------------PHONE VALIDATION-------------------------------------#
        if phonemobile is None or phonehome is None or emergencyhome is None or emergencymobile is None:
            return render_template("register.html", courses=courses, form=form, errormsg="One of the phone numbers is Invalid")

        newStudent=Student(name=request.form['name'],
        last_name=request.form['last_name'],
        email=request.form['email'],
        image_path=filename,
        gender=request.form['gender'],
        inscription_date=request.form['inscription_date'],
        birthdate=request.form['birthdate'],
        phone_mobile=request.form['phone_mobile'],
        phone_home=request.form['phone_home'],
        actual_course=idcourse,
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
        return redirect(url_for('StudentRouting.showStudent'))
    return render_template("register.html", form=form, courses=courses)
