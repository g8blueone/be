from flask import request, Blueprint, make_response

from Application.Model.Doctors import Doctors
from Application.Model.Metadata import Metadata
from Application.Model.Response import Response
from Application.Utils.doctors_query_utils import paginate, get_total_of_pages
from flask import jsonify
from flask_cors import cross_origin

from Application.database import database

doctorapi = Blueprint('doctorapi', __name__)

@cross_origin()
@doctorapi.route('/doctor/', methods=["GET"])
def doctor():
    if request.method == "GET":
        query = request.args
        doctor_id = query.get("id")
        if doctor_id:
            doc = Doctors.query.filter_by(id_doctor=doctor_id).first()
            return jsonify(doc.serialize())
        doctors = paginate(Doctors.query, query)
        response = Response(Metadata(get_total_of_pages(Doctors.query)), doctors)
        return jsonify(response.serialize())
    elif request.method == "PUT":
        new_doctor = request.json
        doctor = Doctors.query.filter_by(id_doctor=new_doctor["id"]).first()
        doctor.first_name = new_doctor["first_name"]
        doctor.last_name = new_doctor["last_name"]
        doctor.address = new_doctor["address"]
        doctor.city = new_doctor["city"]
        doctor.county = new_doctor["county"]
        doctor.country = new_doctor["country"]
        database.session.commit()
        return _corsify_actual_response(jsonify(request.json)), 200
    elif request.method == "OPTIONS":
        return _build_cors_preflight_response()

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response