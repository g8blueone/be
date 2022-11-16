import datetime

def deploy():
    from Application.app import create_app, database
    from Application.Model import Appointments

    app = create_app()
    app.app_context().push()
    database.create_all()

    database.session.add(Appointments.Appointments(1, "Andrei", "Vasile", datetime.date.today(), datetime.datetime.now().time(), "Cardio"))

    database.session.commit()


deploy()
