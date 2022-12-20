import datetime

from flask import request, Blueprint

from Application.Model.Patients import Patients
from Application.database import database
from flask import jsonify
from flask_cors import cross_origin

doctorapi = Blueprint('doctorapi', __name__)

@cross_origin()
@doctorapi.route('/doctor/<id_doctor>', methods=["GET", "PUT"])
def doctor_home(id_doctor):
    if request.method == "GET":
        doctor = Doctors.query.filter_by(id_doctor=id_doctor).first()

        return jsonify(doctor.serialize())

    elif request.method == "PUT":
        new_doctor = request.json

        doctor = Patients.query.filter_by(cnp_patient=cnp).first()
        doctor.email = new_doctor["email"]
        doctor.password = new_doctor["password"]
        doctor.first_name = new_doctor["first_name"]
        doctor.last_name = new_doctor["last_name"]
        doctor.hospital = new_doctor["hospital"]
        doctor.position = new_doctor["position"]
        doctor.specialization = new_doctor["specialization"]

        database.session.commit()
        return jsonify(request.json), 200