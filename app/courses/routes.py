from flask import Flask, render_template, url_for, jsonify, request, redirect
from . import CourseRouting
from database_setup import *
from . import coursesForm
from flask import Blueprint
from flask_login import login_required
from app import login_manager

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

@login_manager.user_loader
def user_loader(id):
    # do whatever you need to to load the user object
    # a database query, for example
    user= session.query(User).filter_by(id=id).one()
    return user

@CourseRouting.route('/course/courseapi')
def CollectingData():
    ArrayCourses = []
    Courses = {}
    Data = {"Allcoursesdata": ArrayCourses}
    coursedata = session.query(Course).all()
    for courses in coursedata:
        Courses["id"] = str(courses.id)
        Courses["name"] = str(courses.name)
        Courses["lesson"] = str(courses.lesson)
        Courses["link"] = str(courses.link)
        ArrayCourses.append(Courses)
        Courses = {}
    return jsonify(Data)

@CourseRouting.route("/course/")
@login_required
def showCourse():
    course=session.query(Course).all()
    print course
    return render_template("course.html", course=course)

@CourseRouting.route("/course/newCourse/", methods=['GET','POST'])
@login_required
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
@login_required
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
@login_required
def deleteCourse(course_id):
    if request.method == 'POST':
        deletedItem = session.query(Course).filter_by(id=course_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('CourseRouting.showCourse'))

    return render_template("deletecourse.html", course_id=course_id)
