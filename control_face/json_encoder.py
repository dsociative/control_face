# -*- coding: utf8 -*-
from datetime import datetime, date
from flask import json


class ControlJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)