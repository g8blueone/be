import datetime

def deploy():
    from Application.app import app
    from Application.database import database
    from Application.Model import Appointments, Patients

    app.app_context().push()
    database.create_all()

    database.session.add(Appointments.Appointments("Andrei Florian", "Vasile Voicescu","Cluj-Napoca", datetime.date.today(), datetime.datetime.now().time(), "Cardiologie"))
    database.session.add(
        Appointments.Appointments("Andrei Vaile", "Vasile Voicescu","Floresti",  datetime.date.today(), datetime.datetime.now().time(), "Cardiologie"))

    database.session.add(
        Appointments.Appointments("Andrei Marian", "Vasile Voicescu", "Flori esti", datetime.date.today(), datetime.datetime.now().time(),
                                  "Neurologie"))

    database.session.add(
        Appointments.Appointments("Zoe Takamura", "Ilie George", "Str. Observatorului nr. 5", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Fizioterapie"))

    database.session.add(
        Appointments.Appointments("Volodymyr Karcenov", "Iulia Maria", "Str. Louis Pasteur nr. 8", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Gastrologie"))

    database.session.add(
        Patients.Patients(1111111111111, "email", "pass", "first", "last", "add", "city", "county", "country", datetime.date.today()))


    database.session.commit()


deploy()
