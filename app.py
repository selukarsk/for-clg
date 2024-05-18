# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import login
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_route():
    username = request.form['username']
    password = request.form['password']
    if login.authenticate(username, password):
        run_main_script()
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid username or password!')
        return redirect(url_for('home'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login.register(username, password):
            flash('Registration successful! Please login.')
            return redirect(url_for('home'))
        else:
            flash('Username already exists!')
            return redirect(url_for('signup'))
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

def run_main_script():
    script_path = os.path.join(os.path.dirname(__file__), 'main.py')
    subprocess.Popen(['python', script_path])

if __name__ == '__main__':
    app.run(debug=True)
