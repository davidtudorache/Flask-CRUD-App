from flask import Blueprint, request, jsonify, redirect, url_for, render_template, flash
from project.models import User
from flask_mysqldb import MySQL

mysql = MySQL()

users = Blueprint('users', __name__)

@users.route('/users/<string:id>', methods=['GET'])
def get(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    data = cur.fetchone()
    cur.close()

    user = {
        'id': data[0],          
        'username': data[1],    
        'email': data[2],      
        'password': data[3],         
        'role': data[4]
    }
    return render_template('edit_user.html', user=user)


@users.route('/users', methods=['GET'])
def getAll():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    return render_template('users.html', users=data)

@users.route('/add', methods=['POST'])
def add():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    new_user = User(username= username, email=email, role=role)
    new_user.set_password(password)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, email, password_hash, role) VALUES (%s, %s, %s, %s)", (new_user.username, new_user.email, new_user.password_hash, new_user.role))

    mysql.connection.commit()
    return redirect(url_for('users.getAll'))

@users.route('/delete/<string:id>', methods=['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect(url_for('users.getAll'))

@users.route('/update/<string:id>', methods=['POST'])
def update(id):
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']

    updated_user = User(username= username, email=email, role=role)
    updated_user.set_password(password)

    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET username=%s, email=%s, password_hash=%s, role=%s WHERE id=%s", (updated_user.username, updated_user.email, updated_user.password_hash, updated_user.role, id))

    mysql.connection.commit()
    return redirect(url_for('users.getAll'))