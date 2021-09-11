from enum import unique
from os import name
import math
from flask import Flask,redirect,render_template,request,session
from flask_sqlalchemy import SQLAlchemy
import json
application=Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///test11.db'
db=SQLAlchemy(application)
application.secret_key = 'super secret key'
with open('login.json','r') as c:
    params=json.load(c)["params"]
class Login(db.Model):
    email=db.Column(db.String(15),unique=True,nullable=False,primary_key=True)
    password=db.Column(db.String(15),nullable=False)


@application.route("/", methods=['GET','POST'])
def login():
    if request.method=='POST':
        em=request.form['email']
        pw=request.form['pwd']
        entry1=Login(email=em,password=pw)
        db.session.add(entry1)
        db.session.commit()
    return render_template("index.html")
@application.route("/dashboard")
def dashboard():
    entry=Login.query.all()
    

    return render_template("logindetail.html",entry=entry)

@application.route("/delete/<string:email>",methods =["GET","POST"])
def delete(email):
    

    entry=Login.query.filter_by(email=email).first()
    db.session.delete(entry)
    db.session.commit()
    return redirect("/dashboard")
@application.route("/login",methods=['GET','POST'])
def signin():
    if request.method=='POST':
        if request.form["email"]==params['userid'] and request.form['pwd']==params['psw']:
            session["user"]=params["userid"]
            entry=Login.query.all()
    

            return render_template("logindetail.html",entry=entry)
    return render_template("login.html")
if (__name__)=="__main__":
    application.run(debug=True,port=1000)