import datetime

from flask import session, request

from Application.app import create_app, database
from datetime import timedelta
from Application.Model.Appointments import Appointments
from Application.Model.Response import Response
from Application.Model.Metadata import Metadata
from flask import jsonify
from flask_cors import CORS, cross_origin
from Application.Utils.appointments_query_utils import query_field_parameters, search_fields, determine_sort_field, paginate, get_total_of_pages

app = create_app()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.before_first_request
def session_handler():
    database.create_all()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@cross_origin()
@app.route('/appointments/', methods=["GET", "POST", "PUT"])
def index():
    if request.method == "GET":
        query = request.query_string.decode()
        query = query.replace("&","=")
        query = query.split("=")
        filtered_appointments = query_field_parameters(Appointments.query, query)
        searched_appointments = search_fields(filtered_appointments, query)
        sorted_appointments = determine_sort_field(searched_appointments, query)
        paginated_appointments = paginate(sorted_appointments, query)
        response = Response(Metadata(get_total_of_pages(sorted_appointments)), paginated_appointments)

        return jsonify(response.serialize())

    elif request.method == "POST":
        new_appointment = request.json
        appointment = Appointments(new_appointment["patient_name"], new_appointment["doctor_name"], new_appointment["location"], datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(new_appointment['time'], '%H:%M').time(), new_appointment["type"])
        database.session.add(appointment)
        database.session.commit()
        return jsonify(request.json), 200

@cross_origin()
@app.route('/appointments/<id>', methods=["DELETE", "PUT"])
def index2(id):
    if request.method == "DELETE":
        Appointments.query.filter_by(id_appointment=int(id)).delete()
        database.session.commit()
        return jsonify(request.json), 200

    elif request.method == "PUT":
        new_appointment = request.json
        appointment = Appointments.query.filter_by(id_appointment=id).first()
        appointment.patient_name = new_appointment["patient_name"]
        appointment.doctor_name = new_appointment["doctor_name"]
        appointment.location = new_appointment["location"]
        appointment.date = datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date()
        appointment.time = datetime.datetime.strptime(new_appointment['time'], '%H:%M').time()
        appointment.type = new_appointment["type"]
        database.session.commit()
        return jsonify(request.json), 200


if __name__ == "__main__":
    app.run(debug=True)
