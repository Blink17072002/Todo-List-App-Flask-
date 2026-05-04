from app import app
from flask import render_template, redirect, url_for
from app.forms import DeleteTaskForm, TodoForm
from app.models import Todo
from app import db

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(task=form.task.data)
        db.session.add(todo)
        # print('Added todo to database')
        db.session.commit()
        return redirect(url_for('home'))
    todo_items = Todo.query.order_by(Todo.timestamp.asc()).all()
    return render_template('home.html', form=form, todo_items=todo_items)

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    form = DeleteTaskForm()
    if form.validate_on_submit():
        d = Todo.query.get_or_404(task_id)
        db.session.delete(d)
        print('deleted todo')
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/toggle/<int:task_id>', methods=['GET', 'POST'])
def toggle_task(task_id):
    task = Todo.query.get(task_id)
    task.is_completed = not task.is_completed
    db.session.commit()
    return redirect(url_for('home'))