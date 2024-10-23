from flask import Flask, request, jsonify, redirect, url_for, render_template, flash
from project import create_app
from flask_mysqldb import MySQL
from project.blueprints.users import users

app = create_app() 
mysql = MySQL(app)

app.register_blueprint(users)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True)