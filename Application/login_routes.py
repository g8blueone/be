import bcrypt
from flask import Blueprint, request, jsonify, make_response
from flask_cors import cross_origin

from Application.Model.Doctors import Doctors
from Application.Model.LoginMeta import LoginMeta
from Application.Model.Patients import Patients
from Application.Model.Response import Response

login_api = Blueprint('login_api', __name__)

@cross_origin()
@login_api.route('/login', methods= ["POST"])
def amazing_diagnostics():
    if request.method == "POST":
        login_info = request.json
        type = ""
        user = Doctors.query.filter_by(email= login_info["email"]).first()
        if user is None:
            user = Patients.query.filter_by(email= login_info["email"]).first()
            if user is None:
                return make_response("Wrong credentials", 400)
            else:
                type = "patient"
        else:
            type = "doctor"
        encoded_password = user.password.encode()

        # generating the salt
        salt = bcrypt.gensalt()

        # Hashing the password
        hash_password = bcrypt.hashpw(encoded_password, salt)

        if bcrypt.checkpw(login_info["password"].encode(), hash_password):
            return make_response("Wrong credentials", 400)

        return Response(LoginMeta((bcrypt.hashpw(user.get_id().encode(), salt), 200), type), [])