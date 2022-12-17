from Application.app import database


class Appointments(database.Model):
    __tablename__ = "Appointments"
    __table_args__ = {'extend_existing': True}

    id_appointment = database.Column(database.Integer, primary_key=True)
    patient_name = database.Column(database.String, nullable=False)
    doctor_name = database.Column(database.String, nullable=False)
    location = database.Column(database.String, nullable=False)
    date = database.Column(database.Date, nullable=False)
    time = database.Column(database.Time, nullable=False)
    type = database.Column(database.String, nullable=False)

    def __init__(self, patient_name, doctor_name, location, appointment_date, appointment_time, appointment_type):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.location = location
        self.date = appointment_date
        self.time = appointment_time
        self.type = appointment_type

    def __str__(self):
        return str(self.id_appointment) + "," + self.patient_name + "," + self.doctor_name + "," + self.location + "," + str(self.date) + "," + str(self.time) + "," + self.type

    def __repr__(self):
        return str(
            self.id_appointment) + "," + self.patient_name + "," + self.doctor_name + "," + self.location + "," + str(
            self.date) + "," + str(self.time) + "," + self.type

    def get_id(self):
        return self.id_appointment

    def serialize(self):
        return {
            "id_appointment": str(self.id_appointment),
            "patient_name": self.patient_name,
            "doctor_name": self.doctor_name,
            "location": self.location,
            "date": str(self.date),
            "time": str(self.time),
            "type": self.type
        }
