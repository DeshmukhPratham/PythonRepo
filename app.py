from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy  #flask sqlalchemy acts as a bridge between flask and the database

app = Flask(__name__)


#www.homerental.com/home
#www.homerental.com/login
#www.homerental.com/register       This are the routes we need to add on our website
#www.homerental.com/dashboard
#www.homerental.com/admin

#we need a decorator to add the routes on our website,we will see what is a decorator
@app.route('/Register')
def Register():
    return render_template('Register.html')
@app.route('/')
@app.route('/Home', methods=['POST','GET'])  #Here we created Home route
def home():
    if request.method == 'POST':
        admin_password ='123456'
        user_name =request.form['username']
        user_password = request.form['password']

    
        if user_name == 'admin':
            if user_password == admin_password:
              return '<h1>Welcome to admin Dashboard</h1>'
            else:
                  return '<h1>Credentials does not match.Please try again after sometine</h1>'
        return '<h1> {user_name} : {user_password} </h1>'
        print(request.form)  #By this we are taking the data from form(for this also we have to write the name attributes)
    else:
         return render_template('home.html')  #we are rendering this from the templates


@app.route('/login') #Here we created login route
def login():
    return render_template('login.html')  #we are rendering this from the templates
if __name__== '__main__':    #this statement means if we are directly calling the file then the app will run
         
         app.run(debug=True) 




