import datetime

def deploy():
    from Application.app import create_app, database
    from Application.Model import Appointments

    app = create_app()
    app.app_context().push()
    database.create_all()

    database.session.add(Appointments.Appointments("Andrei", "Vasile","Cluj-Napoca", datetime.date.today(), datetime.datetime.now().time(), "Cardio"))
    database.session.add(
        Appointments.Appointments("Andrei", "Vasile","Floresti",  datetime.date.today(), datetime.datetime.now().time(), "Cardio"))

    database.session.add(
        Appointments.Appointments("Andrei Marian", "Vasile Voicescu", "Flori esti", datetime.date.today(), datetime.datetime.now().time(),
                                  "Urgente si altele"))
    database.session.commit()


deploy()
