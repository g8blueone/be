import math

from Application.Utils import constants


def paginate(doctors, query):
    try:
        page_position = query.get("page")
        if page_position:
            page = int(page_position)
            return doctors[(page - 1) * constants.pagesize: (page - 1) * constants.pagesize + constants.pagesize]
    except:
        return doctors
    return doctors


def get_total_of_pages(doctors):
    return math.ceil(doctors.count() / constants.pagesize)
