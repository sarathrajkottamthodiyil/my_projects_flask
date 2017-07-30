from flask_wtf import Form  
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class ContactForm(Form):
	name = TextField("Name of student",[validators.Required("Please enter your name.")])
	Gender = RadioField('Gender', choice = [('M','Male'),('F','Female')])
	Address = TextAreaField("Address")

	email = TextField("Email",[validators.Required("Please enter your emil address."),validators.Email("Please enter your email address.")])

	Age = IntegerField("age")
	langauge = SelectField('Langauges',  choice = [('cpp', 'c++', 'python', 'java', 'c')])
	submit = SubmitField("send")


