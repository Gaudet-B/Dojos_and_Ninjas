from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    dojos = Dojo.get_dojos()
    return render_template("index.html", all_dojos = dojos)

@app.route("/new_dojo")
def new_dojo():
    dojos = Dojo.get_dojos()
    return render_template("make_dojo.html", all_dojos = dojos)

@app.route("/add_dojo", methods=['POST'])
def add_dojo():
    data = {
        "name": request.form['dojo_name']
    }
    Dojo.make_dojo(data)
    return redirect("/")

@app.route("/new_ninja")
def new_ninja():
    dojos = Dojo.get_dojos()
    return render_template("make_ninja.html", all_dojos = dojos)

@app.route("/add_ninja", methods=['POST'])
def add_ninja():
    pstatement = request.form
    print(pstatement)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_name']
    }
    Ninja.make_ninja(data)
    return redirect(f"/dojo/{data['dojo_id']}")

@app.route("/dojo/<int:dojo_id>")
def view_dojo(dojo_id):
    data = {
        "id": dojo_id
    }
    dojo = Dojo.get_dojo_name_by_id(data)
    ninjas = Dojo.get_dojos_ninjas(data)
    return render_template("view_dojo.html", all_ninjas = ninjas, dojo = dojo, dojo_id = dojo_id)