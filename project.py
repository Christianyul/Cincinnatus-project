from dependencies import *
from database_setup import *
from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, validators
from wtforms.validators import *
from course import Course


app=Flask(__name__)
app.config['SECRET_KEY'] = "DontTellAnyone"
db_string="postgres://postgres:0321help@localhost:5432/cincinnatus"
engine = create_engine(db_string)
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

#this must be imported later----------------
class CourseForm(Form):
    name = StringField('name', validators=[InputRequired(), Length(min=3,max=30)])
    lesson = IntegerField('lesson', validators=[InputRequired()])
    link= StringField('link', validators=[InputRequired()])



@app.route("/")
@app.route("/course")
def welcome():
    course=session.query(Course).all()
    print course
    return render_template("course.html", course=course)



@app.route("/course/newCourse", methods=['GET','POST'])
def newCourse():
    form = CourseForm()
    if form.validate_on_submit():
        newCourse=Course(name=request.form['name'],lesson=request.form['lesson'], link=request.form['link'])
        session.add(newCourse)
        session.commit()
        # flash("New Item Added")
    return render_template("newcourse.html", form=form)



@app.route("/course/<int:course_id>/editCourse")
def editCourse(course_id):
    form = CourseForm()
    if form.validate_on_submit():
        editCourse=Course(id=course_id, name=request.form['name'],lesson=request.form['lesson'], link=request.form['link'])
        session.add(editCourse)
        session.commit()
        #flash("New Item Added")

        # if request.get:
        #     pass
    return render_template("editcourse.html", form=form)


if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
