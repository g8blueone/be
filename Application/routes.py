import datetime

from flask import render_template, session, request

from Application.app import create_app, database
from datetime import timedelta
from Application.Model.Appointments import Appointments
from flask import jsonify
from flask_cors import CORS, cross_origin
from appointments_query_utils import query_field_parameters, search_fields

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

        return jsonify([appointment.serialize() for appointment in searched_appointments])

    elif request.method == "POST":
        new_appointment = request.json
        appointment = Appointments(new_appointment["patient_name"], new_appointment["doctor_name"], new_appointment["location"], datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date(),
                                   datetime.datetime.strptime(new_appointment['time'], '%H:%M').time(), new_appointment["type"])
        database.session.add(appointment)
        database.session.commit()
        return jsonify(request), 200

    elif request.method == "PUT":
        new_appointment = request.json
        appointment = Appointments.query.filter_by(id_appointment=int(new_appointment["id_appointment"])).first()
        appointment.patient_name = new_appointment["patient_name"]
        appointment.doctor_name = new_appointment["doctor_name"]
        appointment.location = new_appointment["location"]
        appointment.date = datetime.datetime.strptime(new_appointment['date'], '%Y-%m-%d').date()
        appointment.time = datetime.datetime.strptime(new_appointment['time'], '%H:%M').time()
        appointment.type = new_appointment["type"]
        database.session.commit()
        return jsonify(request), 200

@cross_origin()
@app.route('/appointments/<id>/', methods=["DELETE"])
def index2(id):
    Appointments.query.filter_by(id_appointment=int(id)).delete()
    database.session.commit()
    return jsonify(request), 200

@cross_origin()
@app.route('/appointmentslocation=<location>/', methods=["GET"])
def filterByLocation(location):
    appointments = Appointments.query.filter_by(location=location)
    print(appointments)
    return jsonify([appointment.serialize() for appointment in appointments])


'''
@app.route('/<access_level>/profile/student_grades', methods=("GET", "POST"))
@login_required
def grades():
    user = Student.query.filter_by(username=current_user.username).first()
    student_courses = StudentCourse.query.filter_by(student_id=user.student_id).all()
    courses = Course.query.all()

    return render_template('Student/StudentGrades.html',student_courses = student_courses, courses = courses)
'''


if __name__ == "__main__":
    app.run(debug=True)
