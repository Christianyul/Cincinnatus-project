from flask import Flask, render_template, url_for, jsonify, request, redirect, flash
from . import UserRouting
from database_setup import create_engine, db_string, sessionmaker, User
from userForm import UserForm
from flask import Blueprint
import hashlib
from flask_login import login_required
from app import login_manager


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
@login_required
def showUser():
    item=session.query(User).all()
    return render_template("user.html", item=item)

@UserRouting.route("/user/signup/", methods=['GET','POST'])
def signUp():
    form = UserForm()
    h = hashlib.md5() 
    print User
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
@login_required
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
@login_required
def deleteUser(user_id):
    if request.method == 'POST':
        deletedItem = session.query(User).filter_by(id=user_id).one()
        session.delete(deletedItem)
        session.commit()
        return redirect(url_for('UserRouting.showUser'))

    return render_template("deleteuser.html",user_id=user_id)
