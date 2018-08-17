#!/usr/bin/env python3
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/newcreate'
db = SQLAlchemy(app)

class File(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
	content = db.Column(db.Text)
	category= db.relationship('Category',backref=db.backref('files',lazy='dynamic'))
	def __init__(self,title,time,category,content):
		self.title = title
		self.created_time = time
		self.category = category
		self.content = content
	def __repr__(self):
		return '<File %r>' % self.title


class Category(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(80))
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return '<Category %r>' %self.name

@app.route('/')
def index():
	filelist = File.query.all()
	return render_template('index.html',filelist=filelist)
@app.route('/files/<file_id>')
def file(file_id):
	findfile = File.query.filter_by(id=file_id).first()
	if findfile == None:
		abort(404)
	else:
		return render_template('file.html',file=findfile)

