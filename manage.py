import datetime

def deploy():
    from Application.app import create_app, database
    from Application.Model import Appointments

    app = create_app()
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
    database.session.commit()


deploy()
