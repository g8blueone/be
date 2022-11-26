import datetime

from sqlalchemy import or_
from Application.Model.Appointments import Appointments


def query_field_parameters(appointments, query):
    try:
        patient_name_position = query.index("patient")
        patient_name = query[patient_name_position + 1]
        patient_name_list = patient_name.split("%20")
        patient_name_formatted = str()
        for i in patient_name_list:
            patient_name_formatted += i
            patient_name_formatted += " "
        appointments = appointments.filter_by(patient_name=patient_name_formatted[:len(patient_name_formatted) - 1])
    except:
        # no patient filter added
        pass

    try:
        doctor_name_position = query.index("doctor")
        doctor_name = query[doctor_name_position + 1]
        doctor_name_list = doctor_name.split("%20")
        doctor_name_formatted = ""
        for i in doctor_name_list:
            doctor_name_formatted += i
            doctor_name_formatted += " "
        appointments = appointments.filter_by(doctor_name=doctor_name_formatted[:len(doctor_name_formatted) - 1])
    except:
        # no doctor filter added
        pass

    try:
        location_position = query.index("location")
        location = query[location_position + 1]
        location_list = location.split("%20")
        location_formatted = ""
        for i in location_list:
            location_formatted += i
            location_formatted += " "
        appointments = appointments.filter_by(location=location_formatted[:len(location_formatted) - 1])
    except:
        # no location filter added
        pass

    try:
        date_position = query.index("date")
        date = query[date_position + 1]
        appointments = appointments.filter_by(date=datetime.datetime.strptime(date, '%Y-%m-%d').date())
    except:
        # no date filter added
        pass

    try:
        time_position = query.index("time")
        time = query[time_position + 1]
        appointments = appointments.filter_by(time=datetime.datetime.strptime(time, '%H:%M').time())
    except:
        # no time filter added
        pass

    try:
        type_position = query.index("type")
        type = query[type_position + 1]
        type_list = type.split("%20")
        type_formatted = ""
        for i in type_list:
            type_formatted += " "
            type_formatted += i
        appointments = appointments.filter_by(type=type_formatted[:len(type_formatted) - 1])
    except:
        # no type filter added
        pass

    return appointments


def search_fields(appointments, string):
    appointments = appointments.filter(appointments)
