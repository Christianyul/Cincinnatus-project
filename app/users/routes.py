from flask import Flask, render_template, url_for, jsonify, request, redirect, flash
from . import UserRouting
from database_setup import *
from userForm import UserForm
from flask import Blueprint
import hashlib

methods = ['GET', 'POST']
GET, POST = methods

db_string="postgres://postgres:011741@localhost:5432/cincinnatus"
engine = create_engine(db_string)
DBSession=sessionmaker(bind=engine)
session=DBSession()
app=Flask(__name__)

@UserRouting.route("/user/usersapi")
def UserApi():
    users = session.query(User).all()
    Info = []
    Data_Api = {"All_Data": Info}
    for user in users:
        Data = {}
        Data["UserName"] = user.user_name
        Data["Email"] = user.email
        Data["User_Type"] = user.user_type
        Data["Name"] = user.name
        Info.append(Data)
    return jsonify(Data_Api)
    
@UserRouting.route("/user/")
def showUser():
    item=session.query(User).all()
    return render_template("user.html", item=item)

@UserRouting.route("/user/signup/", methods=['GET','POST'])
def signUp():
    form = UserForm()
    h = hashlib.md5() 
    
    if form.validate_on_submit():
        h.update(request.form['password'])

        newItem=User(name=request.form['name'],
        user_name=request.form['user_name'], 
        password=h.hexdigest(),
        email=request.form['email'], 
        user_type=request.form['user_type'] )

        users = session.query(User).filter_by(user_name=request.form['user_name']).all()
        if len(users) >=1:
             flash("Este Usuario ya existe")
             return render_template("signup.html", form=form)   

        if request.form['password'] != request.form['valid']:
            flash("Las passwords no coinciden")
            return render_template("signup.html", form=form)

        session.add(newItem)
        session.commit()
       
        return redirect(url_for('UserRouting.showUser'))
    return render_template("signup.html", form=form)


@UserRouting.route("/user/<int:user_id>/edit/", methods=['GET','POST'])
def editUser(user_id):
    form = UserForm()
    editedItem = session.query(User).filter_by(id=user_id).one()
    if form.validate_on_submit():
        editedItem.name = request.form['name']
        editedItem.user_name = request.form['user_name']
        editedItem.password = request.form['password']
        editedItem.email= request.form['email']
        editedItem.user_type = request.form['user_type']

        session.add(editedItem)
        session.commit()
        #flash("New Item Added")
        return redirect(url_for('UserRouting.showUser'))
    return render_template("edituser.html",form=form, user_id=user_id, item=editedItem)


@UserRouting.route("/user/<int:user_id>/delete/", methods=['GET','POST'])
def deleteUser(user_id):
    if request.method == 'POST':
        deletedItem = session.query(User).filter_by(id=user_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('UserRouting.showUser'))

    return render_template("deleteuser.html",user_id=user_id)
