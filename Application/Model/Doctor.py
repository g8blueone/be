from Application.database import database


class Doctors(database.Model):
    __tablename__ = "Doctors"
    __table_args__ = {'extend_existing': True}

    id_doctor = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String, nullable=False)
    last_name = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False)
    password = database.Column(database.String, nullable=False)
    specialization = database.Column(database.String, nullable=False)
    hospital = database.Column(database.String, nullable=False)
    position = database.Column(database.String, nullable=False)

    def __init__(self, first_name, last_name, email, password, specialization, hospital, position):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.specialization = specialization
        self.hospital = hospital
        self.position = position

    def __str__(self):
        return str(
            self.id_doctor) + "," + self.first_name + "," + self.last_name + "," + self.email + "," + self.password + "," + self.specialization + "," + self.hospital + "," + self.position

    def __repr__(self):
        return str(
            self.id_doctor) + "," + self.first_name + "," + self.last_name + "," + self.email + "," + self.password + "," + self.specialization + "," + self.hospital + "," + self.position

    def get_id(self):
        return self.id_doctor

    def serialize(self):
        return {
            "id_doctor": str(self.id_doctor),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "specialization": self.specialization,
            "hospital": self.hospital,
            "position": self.position
        }
