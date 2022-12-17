import datetime

from flask import request, Blueprint

from Application.Model.Patients import Patients
from Application.database import database
from flask import jsonify
from flask_cors import cross_origin

app2 = Blueprint('app2', __name__)

@cross_origin()
@app2.route('/patient/<cnp>', methods=["GET", "PUT"])
def patient_home(cnp):
    if request.method == "GET":
        patient = Patients.query.filter_by(cnp_patient=cnp).first()

        return jsonify(patient.serialize())

    elif request.method == "PUT":
        new_patient = request.json

        patient = Patients.query.filter_by(cnp_patient=cnp).first()
        patient.email = new_patient["email"]
        patient.password = new_patient["password"]
        patient.first_name = new_patient["first_name"]
        patient.last_name = new_patient["last_name"]
        patient.address = new_patient["address"]
        patient.city = new_patient["city"]
        patient.county = new_patient["county"]
        patient.country = new_patient["country"]
        patient.date_of_birth = datetime.datetime.strptime(new_patient['date_of_birth'], '%Y-%m-%d').date()

        database.session.commit()
        return jsonify(request.json), 200
