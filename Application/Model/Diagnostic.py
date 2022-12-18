from Application.Utils.user_utils import get_user_name
from Application.database import database


class Diagnostic(database.Model):
    __tablename__ = "Diagnostic"
    __table_args__ = {'extend_existing': True}

    id_diagnostic = database.Column(database.Integer, primary_key=True)
    patient_cnp = database.Column(database.String, nullable=False)
    id_appointment = database.Column(database.Integer, database.ForeignKey('Appointments.id_appointment'))
    prescription = database.Column(database.String, nullable=False)
    issue_date = database.Column(database.Date, nullable=False)
    expiration_date = database.Column(database.Date, nullable=False)
    compensated = database.Column(database.Integer, nullable=False) # 0 false/ 1 false

    def __init__(self, patient_cnp, id_appointment, prescription, issue_date, expiration_date, compensated):
        self.patient_cnp = patient_cnp
        self.id_appointment = id_appointment
        self.prescription = prescription
        self.issue_date = issue_date
        self.expiration_date = expiration_date
        self.compensated = compensated

    def __str__(self):
        return str(self.patient_cnp) + ',' + str(self.id_appointment) + "," + self.prescription + "," + str(self.issue_date) + "," +\
               str(self.expiration_date) + "," + str(self.compensated)

    def __repr__(self):
        return str(self.patient_cnp) + ',' + str(
            self.id_appointment) + "," + self.prescription + "," + str(self.issue_date) + "," + \
               str(self.expiration_date) + "," + str(self.compensated)

    def get_id(self):
        return self.id_diagnostic

    def serialize(self):
        return {
            "id_diagnostic": str(self.id_diagnostic),
            "patient_cnp": get_user_name(self.patient_cnp),
            "id_appointment": str(self.id_appointment),
            "prescription": self.prescription,
            "issue_date": str(self.issue_date),
            "expiration_date": str(self.expiration_date),
            "compensated": str(self.compensated)
        }
