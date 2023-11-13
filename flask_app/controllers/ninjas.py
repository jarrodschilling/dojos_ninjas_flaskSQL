from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas', methods=['POST', 'GET'])
def create_ninja():
    if request.method == 'GET':
        dojos = Dojo.get_all()
        return render_template('create-ninja.html', dojos=dojos)
    
    Ninja.create_ninja(request.form)
    dojo_id = request.form.get('dojo_id')
    return redirect(f'/dojos/{dojo_id}')