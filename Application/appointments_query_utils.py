import datetime
import math

from sqlalchemy import or_, desc
from Application.Model.Appointments import Appointments
from Utils import constants


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


def paginate(appointments, query):
    try:
        page_position = query.index("page")
        page = int(query[page_position + 1])
        if page == 1:
            return appointments[page-1:page+constants.pagesize-1]
        if page == get_total_of_pages(appointments):
            return appointments[page+1:page+constants.pagesize]
        return appointments[page:page+constants.pagesize]
    except:
        return appointments


def get_total_of_pages(appointments):
    return math.ceil(appointments.count()/2)


def search_fields(appointments, query):
    try:
        search_position = query.index("search")
        search = query[search_position + 1]
        search_list = search.split("%20")
        search_formatted = ""
        for i in search_list:
            search_formatted += i
            search_formatted += " "
        appointments = appointments.filter(
            or_(Appointments.doctor_name.contains(search_formatted[:len(search_formatted) - 1]),
                Appointments.patient_name.contains(search_formatted[:len(search_formatted) - 1]),
                Appointments.location.contains(search_formatted[:len(search_formatted) - 1]),
                Appointments.type.contains(search_formatted[:len(search_formatted) - 1])))
    except:
        pass

    return appointments

def determine_sort_field(appointments, query):
    try:
        sort_position = query.index("sortField")
        sort_field = query[sort_position + 1]
        match sort_field:
            case "patientField":
                return sort_patient_name(appointments, query)
            case "doctorField":
                return sort_doctor_name(appointments, query)
            case "locationField":
                return sort_location(appointments, query)
            case "dateField":
                return sort_location(appointments, query)
            case "timeField":
                return sort_time(appointments, query)
            case "typeField":
                return sort_type(appointments, query)
    except:
        # no sort field added
        return appointments


def sort_patient_name(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.patient_name)
        else:
            appointments = appointments.order_by(desc(Appointments.patient_name))
    except:
        pass

    return appointments


def sort_doctor_name(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.doctor_name)
        else:
            appointments = appointments.order_by(desc(Appointments.doctor_name))

    except:
        pass

    return appointments


def sort_location(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.location)
        else:
            appointments = appointments.order_by(desc(Appointments.location))

    except:
        pass

    return appointments


def sort_date(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.date)
        else:
            appointments = appointments.order_by(desc(Appointments.date))

    except:
        pass

    return appointments


def sort_time(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.time)
        else:
            appointments = appointments.order_by(desc(Appointments.time))

    except:
        pass

    return appointments


def sort_type(appointments, query):
    try:
        sort_mode = query.index("sortMode")
        sort = query[sort_mode + 1]
        if sort == "ASC":
            appointments = appointments.order_by(Appointments.type)
        else:
            appointments = appointments.order_by(desc(Appointments.type))

    except:
        pass

    return appointments
