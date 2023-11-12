from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas', methods=['POST', 'GET'])
def create_ninja():
    if request.method == 'GET':
        return render_template('create_ninja.html')
    return redirect('/dojos')