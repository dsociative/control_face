# -*- coding: utf8 -*-
from flask.helpers import json
from wtforms import Form


class ControlCommand(object):

    class CommandForm(Form):
        pass

    def __init__(self, request_form):
        self.result = {}
        self.form = self.get_form(request_form)

    def get_form(self, request_form):
        return self.CommandForm(request_form)

    def execute(self):
        return

    def set_result(self, result):
        self.result = result

    def pretty(self):
        return json.dumps(self.result, sort_keys=True, indent=4,
                          separators=(',', ': '))

