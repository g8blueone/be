import datetime

from Application.Model import Diagnostic


def deploy():
    from Application.app import app
    from Application.database import database
    from Application.Model import Appointments, Patients

    app.app_context().push()
    database.create_all()

    database.session.add(
        Patients.Patients("1", "amazing@fakeemail.com", "1234", "Yuki", "Takamura", "Str. Observatorului nr. 15", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date.today()))

    database.session.add(
        Patients.Patients("2", "lkols@fakeemail.com", "12345", "Ellen", "Rebreanu", "Str. Observatorului nr. 17",
                          "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date.today()))

    database.session.add(Appointments.Appointments("1", "Vasile Voicescu","Cluj-Napoca", datetime.date.today(), datetime.datetime.now().time(), "Cardiologie"))
    database.session.add(
        Appointments.Appointments("1", "Vasile Voicescu","Floresti",  datetime.date.today(), datetime.datetime.now().time(), "Cardiologie"))

    database.session.add(
        Appointments.Appointments("2", "Vasile Voicescu", "Flori esti", datetime.date.today(), datetime.datetime.now().time(),
                                  "Neurologie"))

    database.session.add(
        Appointments.Appointments("1", "Ilie George", "Str. Observatorului nr. 5", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Fizioterapie"))

    database.session.add(
        Appointments.Appointments("2", "Iulia Maria", "Str. Louis Pasteur nr. 8", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Gastrologie"))

    database.session.add(
       Diagnostic.Diagnostic("1", 1, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",datetime.date.today(), datetime.date.today(), 1))

    database.session.add(
        Diagnostic.Diagnostic("2", 2, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",
                              datetime.date.today(), datetime.date.today(), 1))

    database.session.commit()


deploy()
