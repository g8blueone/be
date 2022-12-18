import datetime

from Application.Model import Diagnostic


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
       Diagnostic.Diagnostic("11234", 1, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",datetime.date.today(), datetime.date.today(), 1))

    database.session.add(
        Diagnostic.Diagnostic("55555", 2, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",
                              datetime.date.today(), datetime.date.today(), 1))
    database.session.add(Patients.Patients(1111111111111, "email", "pass", "first", "last", "add", "city", "county", "country", datetime.date.today()))

    database.session.commit()


deploy()
