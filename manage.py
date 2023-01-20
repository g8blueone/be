import datetime

import bcrypt

from Application.Model import Diagnostic


def deploy():
    from Application.app import app
    from Application.database import database
    from Application.Model import Appointments, Patients, Doctors

    app.app_context().push()
    database.create_all()

    database.session.add(
        Patients.Patients("1", "amazing@fakeemail.com", str(bcrypt.hashpw("1234".encode(), bcrypt.gensalt())), "Yuki", "Takamura", "Str. Observatorului nr. 15", "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date.today()))

    database.session.add(
        Patients.Patients("2", "lkols@fakeemail.com", "12345", "Ellen", "Rebreanu", "Str. Observatorului nr. 17",
                          "Cluj-Napoca", "Cluj", "Romania",
                          datetime.date.today()))

    database.session.add(Appointments.Appointments("1", "D1","Cluj-Napoca", datetime.date.today(), datetime.datetime.now().time(), "Regular Control"))
    database.session.add(
        Appointments.Appointments("1", "D1","Floresti",  datetime.date.today(), datetime.datetime.now().time(), "Regular Control"))

    database.session.add(
        Appointments.Appointments("2", "D2", "Flori esti", datetime.date.today(), datetime.datetime.now().time(),
                                  "Surgery"))

    database.session.add(
        Appointments.Appointments("1", "D3", "Str. Observatorului nr. 5", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Surgery"))

    database.session.add(
        Appointments.Appointments("2", "D2", "Str. Louis Pasteur nr. 8", datetime.date.today(),
                                  datetime.datetime.now().time(),
                                  "Consulation"))

    database.session.add(
       Diagnostic.Diagnostic(1, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",datetime.date.today(), datetime.date.today(), 1))

    database.session.add(
        Diagnostic.Diagnostic(2, "Nurofen Max 200mg 1 after lunch, Agocalmin 50mg in the morning",
                              datetime.date.today(), datetime.date.today(), 1))

    database.session.add(
        Doctors.Doctors("D1", "Johnny", "Test","Mail@gmail.com" ,str(bcrypt.hashpw("Parola".encode(), bcrypt.gensalt())), "Cardiology", "Sf Parascheva", "Surgeon")
    )

    database.session.add(
        Doctors.Doctors("D2", "Johnny", "Bravo","Mail@gmail.com", "Parolsa", "Cardiology", "Sf Parascheva", "Surgeon")
    )

    database.session.add(
        Doctors.Doctors("D3", "Johnny", "Smith","Mail@gmail.com", "Parolsa", "Cardiology", "Sf Parascheva", "Surgeon")
    )

    database.session.add(
        Doctors.Doctors("D4", "Johnny", "Doe","Mail@gmail.com", "Parolsa", "Neurology", "Sf Parascheva", "Surgeon")
    )

    database.session.add(
        Doctors.Doctors("D5", "Johnny", "Cash","Mail@gmail.com", "Parolsa", "Cardiology", "Spitalul de Boli Infectioase", "Surgeon")
    )

    database.session.commit()


deploy()
