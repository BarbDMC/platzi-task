import unittest
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm, TodoForm, DeleteForm, UpdateTodoForm, UpdateTodoDoneForm
from app.firestore_service import get_users, get_todos, put_todo, delete_todo, update_todo, update_todo_to_done

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    response = make_response(redirect('/dashboard'))

    return response


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required

def dashboard():
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteForm()
    update_todo_form =  UpdateTodoForm()
    update_todo_done_form = UpdateTodoDoneForm()

    context = {
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_todo': update_todo_form,
        'update_todo_done_form': update_todo_done_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        flash('Tarea creada con éxito')
        return redirect(url_for('dashboard'))

    

    return render_template('dashboard.html', **context)

@app.route('/todos/delete/<todo_id>',  methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id= user_id, todo_id= todo_id)

    return redirect(url_for('dashboard'))

@app.route('/todos/update_todo/<todo_id>/<description>',  methods=['POST'])
def update(todo_id, description):
    user_id = current_user.id
    update_todo_form =  UpdateTodoForm()

    if update_todo_form.validate_on_submit():
        update_todo(user_id= user_id, todo_id= todo_id, description= update_todo_form.description.data)
        flash('Tarea actualizada con éxito')
        return redirect(url_for('dashboard'))



@app.route('/todos/update_done/<todo_id>/<int:done>',  methods=['POST'])
def update_todo_done(todo_id, done):
    user_id = current_user.id
    update_todo_to_done(user_id= user_id, todo_id= todo_id, done= done)

    return redirect(url_for('dashboard'))
