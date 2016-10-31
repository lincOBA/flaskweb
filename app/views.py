#-*- coding:utf-8 -*-
from datetime import datetime
from flask import render_template,flash,redirect,session,url_for, request, g
from flask.ext.login import login_user, logout_user,current_user, login_required
from models import  Message,lv,uUser,Post,ROLE_USER,ROLE_ADMIN
from app import app,db,lm
from forms import LoginForm, SignUpForm, LvForm
@app.route('/',methods=['GET','POST'])
def home():
    return redirect(url_for('login'))
@app.route('/index',methods=['GET','POST'])
def index():
    nick = request.args.get('nickname')
    if not nick:
        nick = "An anonymous"
    if request.method == 'POST' and request.form.get('message') != None:
        uName = nick
        uMsg = request.form.get('message')
        uMessage = Message(name = str(uName), msg = str(uMsg), time = str(datetime.now()))
        flash(uMessage.time+"|"+uMessage.name+":"+uMessage.msg)
        db.session.add(uMessage)
        db.session.commit()
            
    return render_template("index.html",\
            nickname=nick,\
            posts = Post.query.all(),\
            msgs = Message.query.filter(Message.name!='None').order_by(Message.id.desc()))
@app.route('/rent')
def rent():
    return render_template("rent.html")
@app.route('/users')
def users():
    return render_template("users.html",users = uUser.query.all())
@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    
    form = SignUpForm()
    user = uUser()
    if form.validate_on_submit():
        user_name = request.form.get('name')
        user_password = request.form.get('password')
        register_check = uUser.query.filter(db.or_(uUser.nickname == user_name,uUser.password == '123456')).first()
        if register_check:
            flash("error:The user's name or email already exists!")
            return redirect('/sign-up')
        if len(user_name) and len(user_password):
            user.nickname = user_name
            user.password = user_password
            user.role = ROLE_USER
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/sign-up')
            flash("Sign up successful!")
            return render_template('index.html',nickname=user_name)
    return render_template('sign_up.html',form = form)
@app.route('/gaode')
def gaode():
    return render_template("gaode.html")
@app.route('/searchdan', methods = ['GET', 'POST'])
def searchdan():
    uId = request.form.get('search')
    flash(uId)
    return render_template("searchdan.html",lvs = lv.query.filter(lv.id==uId))
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('index')
    form = LoginForm()
    if form.validate_on_submit():
        user = uUser.login_check(request.form.get('name'),request.form.get('password'))
        flash(request.form.get('name'))
        if user:
            #login_user(user)
            #user.last_seen = datetime.datetime.now()
            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')
            flash('Login requested for Name: ' + form.name.data)
            flash('passed: ' + str(form.password.data))
            flash('remember_me: ' + str(form.remember_me.data))
            return redirect(url_for("index",nickname=form.name.data))
        else:
            flash('Login failed, Your name is not exist!')
            return redirect('/login')

    return render_template('login.html',title = 'Sign In',form = form)
@app.route('/dan',methods=['GET','POST'])
def dan():
    form = LvForm()
    flash(form.name.data)
    flash("Do it?"+str(form.validate_on_submit()))
    if request.method=='POST':
        uName = request.form.get('name')
        uDepartment = request.form.get('department')
        uJob = request.form.get('job')
        uTime1 = request.form.get('time1')
        uTime2 = request.form.get('time2')
        uGenre = request.form.get('genre')
        uReason = request.form.get('reason')
        flash("Leave name:" + uName)
        flash("Department:" + uDepartment)
        flash("Job:" + uJob)
        flash("Leave time"+uTime1)
        flash(uTime2)
        flash(uGenre)
        flash(uReason)
        if uName:
            uLv = lv(name = uName,\
                department = uDepartment,\
                job = uJob,\
                time1 = uTime1,\
                time2 = uTime2,\
                genre = uGenre,\
                reason = uReason)
            try:
                db.session.add(uLv)
                db.session.commit()
            except:
                flash("The Databse error!")
                return redirect('/index')
            flash("Commit successful!")
    return render_template('dan.html',form=form)
@app.route('/dans')
def dans():
    return render_template('dans.html',lvs = lv.query.all())
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
