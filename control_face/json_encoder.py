# -*- coding: utf8 -*-
from datetime import datetime, date
from flask import json


def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


class ControlJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)