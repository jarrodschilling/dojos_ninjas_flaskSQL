from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def show_all_dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos=dojos)

@app.route('/dojos/<int:dojo_id>')
def show_one_dojo(dojo_id):
    dojo = Dojo.show_one_with_ninjas(dojo_id)
    return render_template('show-dojo.html', dojo=dojo_id)