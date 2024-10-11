from flask import Blueprint, request, url_for, redirect, render_template, session

hello_controller = Blueprint('hello', __name__)

@hello_controller.route('/', methods=['post', 'get'])
def index():
    return render_template('home.html')

@hello_controller.route('/login', methods=['post', 'get'])
def login():
   
    return render_template('login.html')

    