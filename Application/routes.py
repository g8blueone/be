
from flask import render_template, session

from Application.app import create_app, database
from datetime import timedelta
from Application.Model.Appointments import Appointments
from flask import jsonify

app = create_app()

@app.before_first_request
def session_handler():
    database.create_all()
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)


@app.route('/', methods=["GET"])
def index():
    appointments = Appointments.query.all()
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
