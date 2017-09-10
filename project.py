from dependencies import *
from database_setup import *
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequire
from course import Course

app=Flask(__name__)
db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
Base.metadata.bind = engine
DBSession=sessionmaker(bind=engine)
session=DBSession()


@app.route("/")
def Welcome():
    # items=session.query(Student).all()
    # return jsonify(Student=[i.serialize for i in items])
    return "Hola"


#@app.route("/courses/newCourse", methods=['GET','POST'])



if __name__ == '__main__':
    app.secret_key='super_secret_key'
    app.debug = True
app.run(host='0.0.0.0', port=5000)
