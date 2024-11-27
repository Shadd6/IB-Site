from flask import Flask, jsonify
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)  # __name__ здесь используется правильно


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
  return 'This is the about page'

@app.route('/user/<username>')
def show_user_profile(username):
  return f'User {username}'

@app.route('/hello/<name>')
def hello(name):
  return render_template('hello.html', name=name)

@app.route('/greet/<name>')
def greet(name):
  return f'Hello, {name}!'

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
  name = request.form['name']
  return f'Hello, {name}'

@app.route('/data')
def data():
    return jsonify({'key': 'value'})



if __name__ == '__main__':  # Здесь тоже __name__
    app.run(debug=True)
