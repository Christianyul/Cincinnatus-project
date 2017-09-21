from flask import Flask, render_template, url_for
from . import StudentRouting
from database_setup import *
from studentForm import StudentForm
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


@StudentRouting.route("/student/")
def showStudent():
    item=session.query(Student).all()
    print item
    return render_template("student.html", item=item)


@StudentRouting.route("/student/register/", methods=['GET','POST'])
def newStudent():
    form = StudentForm()
    if form.validate_on_submit():
        # filename = secure_filename(request.form['image_path'])
        # print os.path.realpath(filename)
        # file.save(os.path.join('/static/Pictures', filename))
        print form.errors
        print "its happening 2"
        newItem=Student(name=request.form['name'],
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


        session.add(newItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('StudentRouting.showStudent'))

        # try:
        #     con = connect(user='postgres', host = 'localhost', password='011741')
        #     con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        #     cur= con.cursor()
        #     SQL = """INSERT INTO students (name,last_name, email, gender,inscription_date, ending_date, retirement_date,
        #     birthdate, phone_mobile, phone_home, id_document, status, marital_status, nationality, address)
        #     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        #
        #     data = (request.form['name'],
        #     request.form['last_name'],
        #     request.form['email'],
        #     request.form['gender'],
        #     request.form['inscription_date'],
        #     request.form['ending_date'],
        #     request.form['retirement_date'],
        #     request.form['birthdate'],
        #     request.form['phone_mobile'],
        #     request.form['phone_home'],
        #     request.form['id_document'],
        #     request.form['status'],
        #     request.form['marital_status'],
        #     request.form['nationality'],
        #     request.form['address']
        #     )
        #
        #     cur.execute(SQL, data)
        #
        #     cur.close()
        #     con.close()
        #
        #     return redirect(url_for('StudentRouting.showStudent'))

        # except Exception as e:
        #  raise
    print "its happening 1"

    return render_template("studentsignup.html", form=form)




@StudentRouting.route("/student/<int:student_id>/edit/", methods=['GET','POST'])
def editStudent(student_id):
    form = StudentForm()
    editedItem = session.query(Student).filter_by(id=student_id).one()
    if form.validate_on_submit():
        editedItem.name = request.form['name']
        editedItem.last_name=request.form['last_name']
        editedItem.email=request.form['email']
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
