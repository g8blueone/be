import datetime

from flask import request, Blueprint

from Application.Model.Doctors import Doctors
from Application.Model.Metadata import Metadata
from Application.Model.Response import Response
from Application.Utils.doctors_query_utils import *
from flask import jsonify
from flask_cors import cross_origin

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
        filtered_doctors = query_field_parameters(Doctors.query, query)
        searched_doctors = search_fields(filtered_doctors, query)
        sorted_doctors = determine_sort_field(searched_doctors, query)
        paginated_doctors = paginate(sorted_doctors, query)
        response = Response(Metadata(get_total_of_pages(Doctors.query)), paginated_doctors)
        return jsonify(response.serialize())