from database_setup import *
#all other dependencies are imported from database_setup
from course import Course
from courseRouting import CourseRouting, app
from flask import Blueprint





# app.config['SECRET_KEY'] = "DontTellAnyone"
#cambiar clave
# db_string="postgres://postgres:0321help@localhost:5432/cincinnatus"
# engine = create_engine(db_string)
# Base.metadata.bind = engine
# DBSession=sessionmaker(bind=engine)
# session=DBSession()

#CRUD CURSOS
@app.route("/")
def welcome():
    return "Hello"


app.register_blueprint(CourseRouting, url_prefix='/course')




if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
