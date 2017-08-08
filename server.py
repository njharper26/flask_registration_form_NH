from flask import Flask, session, request, redirect, render_template, flash
import re

app = Flask(__name__)
app.secret_key = 'd41d8cd98f00b204e9800998ecf8427e'
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index(): 
    
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    
    session['color'] = 'red'
    fail = False

    if len(request.form['email']) < 1:
        flash("** Must include Email **", 'error')
        fail = True
    elif not email_regex.match(request.form['email']):
        flash("**Email must be a vaild email address**", 'error')
        fail = True
    
    if len(request.form['first']) < 1:
        flash("** Must include First Name **")
        fail = True
    elif not request.form['first'].isalpha():
        flash("** First Name cannot include numbers or special characters (alpha only) **")
        fail = True

    if len(request.form['last']) < 1:
        flash("** Must include Last Name **")
        fail = True
    elif not request.form['last'].isalpha():
        flash("** Last Name cannot include numbers or special characters (alpha only) **")
        fail = True

    if len(request.form['pass']) < 1:
        flash("** Must include a password with a minimum of 9 characters **")
        fail = True
    elif len(request.form['pass']) < 9:
        flash("** Mininum password length is 9 characters **")
        fail = True

    if len(request.form['pass_confirm']) < 1:
        flash("** Must confirm password **")
        fail = True
    elif session['pass'] != request.form['pass_confirm']:
        flash("** Passwords must match **")
        fail = True
    
    if len(request.form['dob']) < 1:
        flash("** Must include Date of Birth **")
        fail = True

    if fail == False:
        flash("Successfully Registered. THANK YOU!!!", 'success')
        session['color'] = 'green'

    return redirect('/')
    
app.run(debug=True)