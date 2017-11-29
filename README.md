# **Steps to Install**

## **1.** Install PostgreSQL
https://www.postgresql.org/.

Note: A GUI manager like PgAdmin(Free) or EMS Sql(premium) is recommended. 

## **2.** Install Python 2.7

This project is not yet supported on python 3.

## **3.** Install the libraries in the requirements.txt file

Just go to the the file location and run pip install -r requirements.txt on your terminal. 

## **4.** Set up the app

**4.1** Go to the app's directory you should see a file called run.py 

**4.2** Go to the dependencies.py file and change the database variables with your current user, password, port and database name for postgresql 

**4.3** In your terminal run "python run.py"

you should see something in your terminal telling you that the app is running and the text "Database Setup Done"

**4.4** Check that your database is correctly setted (with all the tables on it) 

IF FOR SOME REASON you dont see any tables in your database, delete the current database and check your database_setup.py file then try again

**4.5** Access your localhost in the 5000 port by default (localhost:5000) 

**4.6** Create an user in /user/signup 
 
DO NOT Create an user directly in the database since the login ask for the password hashed
 
**4.7** Create at least 1 Course

It could be from the route /courses or the database itself

Now you are ready to go

# Useful Documentation

This project is based on a blueprint arquitecture read more about flask blueprint here: https://damyanon.net/post/flask-series-structure/

Everything about flask forms here: https://www.youtube.com/watch?v=eu0tg4vgFr4&list=PLXmMXHVSvS-C_T5JWEDWIc9yEM3Hj52-1

Uploading files with flask: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

Remember that you can find about any library mentioned in the requirements.txt file by just googling it