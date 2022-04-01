from asyncio import tasks
from flask import Flask, render_template, session

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/project_tracker'
app.config['SECRET_KEY'] = (r'\xa5\x9f\xe7o\xb9\xfe\x06\xcb\x9e\'4SX\xd0|\x8b:\xa8\xde\xb7\xc3F')

db = SQLAlchemy(app)

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))

class Task(db.Model):
    __tablename__ = 'projects'
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))
    project = db.relationship("Project")

@app.route("/")
def show_projects():
    return render_template("index.html", projects=Project.query.all())

@app.route("/projects/<projects_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html",
    project=Project.query.filter_by(project_id=project_id).first(),
    tasks=Task.query.filter_by(project_id=project_id).all()
    )

@app.route("/add/project", methods=['POST'])
def add_project():
    return "added"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task():
    return "task added"

app.run(debug=True, host="127.0.0.1", port=3000)