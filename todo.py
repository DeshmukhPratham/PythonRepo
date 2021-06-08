from flask import Flask, render_template, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'XDSWCW5TDYJEDSHTGRS'

db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    todo = db.Column(db.String(200))
    is_completed = db.Column(db.Boolean)


    


	def __init__(self, todo_v):
		self.todo = todo_v
		self.is_completed = False

@app.route('/add', methods=['POST'])
def add_todo():
	new_todo = request.form['todo']
	obj = Data(new_todo)
	db.session.add(obj)
	db.session.commit()

	# flash('Todo is added!!')
	flash('Todo is added!!', 'success')
	return redirect(url_for('home'))

@app.route('/edit', methods=['POST'])
def edit_todo():
	id_m = request.form["todo_id_m"]
	todo_m = request.form["todo_m"]
	
	todo_c = Data.query.get(id_m)

	todo_c.todo = todo_m

	db.session.commit()
	flash('Todo modified successfully!!', 'success')
	return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete_todo(id):
	todo_d = Data.query.get(id)
	db.session.delete(todo_d)
	db.session.commit()
	flash('Todo successfully deleted!!', 'success')
	return redirect(url_for('home'))

@app.route('/completed/<id>')
def complete_todo(id):
	todo = Data.query.get(id)
	todo.is_completed = True
	db.session.commit()
	flash(f'{todo.todo} is completed!!', 'success')
	return redirect(url_for('home'))

@app.route('/notcompleted/<id>')
def not_complete_todo(id):
	todo = Data.query.get(id)
	todo.is_completed = False
	db.session.commit()
	return redirect(url_for('home'))

@app.route('/filter/<int:num>')
def filter_todo(num):
	if num == 1:
		return redirect(url_for('home'))
	elif num == 2:
		todos = Data.query.filter_by(is_completed = False)
		return render_template('home.html', todos = todos)
	elif num == 3:
		todos = Data.query.filter_by(is_completed = True)
		return render_template('home.html', todos = todos)

@app.route('/')
def home():
	todos = Data.query.all()
	return render_template('home.html', todos=todos)

if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
