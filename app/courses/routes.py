from flask import Flask, render_template, url_for
from . import CourseRouting 
from database_setup import *
from . import coursesForm
from flask import Blueprint

methods = ['GET', 'POST']
GET, POST = methods

nl = "\n"

db_string="postgres://postgres:0321help@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

def CollectingData():
    Data = {}
    coursedata = session.query(Course).all()
    for courses in coursedata:
        Data["id"] = courses.id
        Data["name"] = courses.name
        Data["lesson"] = courses.lesson
        Data["link"] = courses.link
    return Data

@CourseRouting.route("/course/")
def showCourse():
    course=session.query(Course).all()
    print course
    return render_template("course.html", course=course)


@CourseRouting.route("/course/newCourse/", methods=['GET','POST'])
def newCourse():
    form = coursesForm.CourseForm()
    if form.validate_on_submit():
        newCourse=Course(name=request.form['name'],lesson=request.form['lesson'], link=request.form['link'])
        session.add(newCourse)
        session.commit()
        # flash("New Item Added")
        return redirect(url_for('CourseRouting.showCourse'))
    return render_template("newcourse.html", form=form)


@CourseRouting.route("/course/<int:course_id>/edit/", methods=['GET','POST'])
def editCourse(course_id):
    form = coursesForm.CourseForm()
    editedItem = session.query(Course).filter_by(id=course_id).one()
    if form.validate_on_submit():
        editedItem.name = request.form['name']
        editedItem.lesson = request.form['lesson']
        editedItem.link = request.form['link']
        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('CourseRouting.showCourse'))
    return render_template("editcourse.html",form=form, course_id=course_id, item=editedItem)


@CourseRouting.route("/course/<int:course_id>/delete/", methods=['GET','POST'])
def deleteCourse(course_id):
    if request.method == 'POST':
        deletedItem = session.query(Course).filter_by(id=course_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('CourseRouting.showCourse'))

    return render_template("deletecourse.html", course_id=course_id)
