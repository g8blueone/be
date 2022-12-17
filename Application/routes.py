import datetime

from flask import session, request

from Application.Utils.diagnostics_query_utils import get_diagnostic
from Application.app import create_app, database
from datetime import timedelta
from Application.Model.Appointments import Appointments
from Application.Model.Diagnostic import Diagnostic
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
@app.route('/appointments/', methods=["GET", "POST"])
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

@cross_origin()
@app.route('/diagnostics/', methods= ["GET", "POST"])
def amazing_diagnostics():
    if request.method == "GET":
        query = request.query_string.decode()
        query = query.replace("&", "=")
        query = query.split("=")
        diagnostic = []
        diagnostic.append(get_diagnostic(query))
        if diagnostic != 0:
            response = Response(Metadata(1), diagnostic)
            return jsonify(response.serialize())
        else:
            return 404

    elif request.method == "POST":
        new_diagnostic = request.json
        Diagnostic.query.filter_by(id_appointment=new_diagnostic['id_appointment']).delete()
        database.session.commit()
        diagnostic = Diagnostic(new_diagnostic["patient_cnp"], int(new_diagnostic["id_appointment"]),
                                new_diagnostic["prescription"], datetime.datetime.strptime(new_diagnostic["issue_date"],'%Y-%m-%d').date(),
                                datetime.datetime.strptime(new_diagnostic["expiration_date"],'%Y-%m-%d').date(),
                                int(new_diagnostic["compensated"]))
        database.session.add(diagnostic)
        database.session.commit()
        return jsonify(request.json), 200


if __name__ == "__main__":
    app.run(debug=True)
