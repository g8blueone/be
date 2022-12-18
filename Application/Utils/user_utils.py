from Application.Model import Patients


def is_doctor(id):
    if id[0] == "D":
        return True
    return False


def get_user_name(id):
    if not is_doctor(id):
        user = Patients.Patients.query.filter_by(cnp_patient=id).first()
        return user.first_name + " " + user.last_name
