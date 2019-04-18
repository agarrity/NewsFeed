from flask import Flask, jsonify, render_template, Response, redirect, request, url_for, session

app = Flask(__name__)

USERNAME_TOKEN = 'username'
app.secret_key = b'dAwS74r!DP/'

@app.route('/')
def index():
    if USERNAME_TOKEN in session:
        return render_template('index.html')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form[USERNAME_TOKEN]
    if request.form[USERNAME_TOKEN] == "a":
        session[USERNAME_TOKEN] = username
        return redirect(url_for('index'))
    return Response("{'a':'b'}", status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)