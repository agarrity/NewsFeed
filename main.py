import datetime
from flask import Flask, jsonify, render_template, Response, redirect, request, url_for, session
from dataAccess import getUser, addNewUser, addNewFavorite, getFavorites

app = Flask(__name__)

USERNAME_TOKEN = 'username'
PASSWORD = 'password'
LASTLOGIN = 'lastlogin'
FAVORITE = 'favorite'
app.secret_key = b'dAwS74r!DP/'

@app.route('/')
def index():
    if USERNAME_TOKEN in session:
        return render_template('index.html', lastLogin = session[LASTLOGIN])
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form[USERNAME_TOKEN]
    user = getUser(username, request.form[PASSWORD])
    if user != None:
        session[USERNAME_TOKEN] = username
        session[LASTLOGIN] = user[LASTLOGIN]
        return redirect(url_for('index'))
    return Response("{'errorMessage':'Invalid username or password'}", status=400, mimetype='application/json')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()        
    return redirect(url_for('index'))

@app.route('/newUser', methods=['POST', 'GET'])
def newUser():
    if (request.method == 'GET'):
        return render_template('/createAccount.html')
    username = request.form[USERNAME_TOKEN]
    user = addNewUser(username, request.form[PASSWORD])
    if user != None:
        session[USERNAME_TOKEN] = username
        session[LASTLOGIN] = user[LASTLOGIN]
        return redirect(url_for('index'))
    return Response("{'errorMessage':'Already a user with that name'}", status=400, mimetype='application/json')

@app.route('/favorite', methods=['POST', 'GET'])
def favorite():
    if (request.method == 'GET'):
        fav = getFavorites(session[USERNAME_TOKEN])
        favorites = ', '.join(fav)
        return jsonify(fav)

    username = session[USERNAME_TOKEN]
    favorite = request.form[FAVORITE]
    addNewFavorite(username, favorite)
    return Response("{'success':'added to favorites'}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run('0.0.0.0', port=7213)