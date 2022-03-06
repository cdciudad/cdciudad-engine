from typing import Dict
from uuid import UUID
from datetime import date, datetime


def serialize(d: Dict):
    for key in d:
        val = d[key]
        # For nested objects
        if type(val) is dict:
            serialize(val)
            continue
        if type(val) in [UUID, datetime, date]:
            d[key] = str(val)
    return d


def check_last_week(creation_date):
    creation_date = datetime.strptime(creation_date, "%Y-%m-%d %H:%M:%S.%f")
    today = datetime.now()
    return (today - creation_date).days < 7
