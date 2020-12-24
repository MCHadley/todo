from flask import Flask, request, Response
from .task import Task
from .user import User

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>You are connected to the todo app</h1>'

@app.route('/new', methods=['POST'])
def add_task():
    return 'New'