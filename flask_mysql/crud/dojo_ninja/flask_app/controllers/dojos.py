from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# Redirect index page #
@app.route('/')
def index():
    return redirect('/dojos')

# Home page #
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos = dojos)

# Create Dojo #
@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

#Show dojo info #
@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_in_dojo(data)
    return render_template("show_dojo.html", dojo = dojo, ninjas = ninjas)

# New ninja #
@app.route('/ninjas')
def new_ninja():
    dojos= Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojos)

# Ninja Form Post  redirect #
@app.route('/new', methods=['POST'])
def new():
    print(request.form)
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.save(data)
    return redirect('/dojos')