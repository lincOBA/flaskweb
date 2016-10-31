#-*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField,TextAreaField,DateTimeField,SelectField
from wtforms.validators import Required,Email,Length

class LoginForm(Form):
    name = TextField('Name', validators=[Required(),Length(max=15)])
    password = PasswordField('password', validators = [Required()])
    remember_me = BooleanField('Remember_me',default = False)
    submit = SubmitField('Log in')

class SignUpForm(Form):
    name = TextField('Name', validators=[Required(),Length(max=15)])
    password = PasswordField('password', validators = [Required()])
    submit = SubmitField('Sign up')
class LvForm(Form):
    name= TextField('name',validators = [Required(),Length(max=15)])
    department = TextField('department',validators =[Required(),Length(max=15)])
    job = TextField('job',validators = [Required(),Length(max=15)])
    time1 = DateTimeField('time1',format = '%m/%d/%y',validators=[Required()])
    time2 = DateTimeField('time2',format = '%m/%d/%y',validators=[Required()])
    genre = SelectField('genre',\
	validators = [Required()],\
    	choices = [('gj',u'工假'),\
	            ('ggj',u'公假'),\
                    ('bj',u'病假'),\
                    ('sj',u'事假')])
    reason = TextAreaField('reason',validators = [Required(),Length(max=150)])
    submit = SubmitField('Lv')
