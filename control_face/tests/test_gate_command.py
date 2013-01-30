# -*- coding: utf8 -*-
from datetime import datetime
from flask.helpers import json
from werkzeug.datastructures import MultiDict
from control_face.tests.base_test import BaseTest
from control_face.tests.test_env.commands.command_something_else import CommandSomethingElse


class TestGateCommand(BaseTest):

    def setUp(self):
        self.command = CommandSomethingElse(MultiDict({'what': ['whatever']}))

    def test_execute(self):
        self.eq(self.command.execute(), None)
        self.eq(self.command.result, {'this': {'is': ['response', 'long']}})

    def test_set_result(self):
        self.command.set_result(['result'])
        self.eq(self.command.result, ['result'])

    def test_pretty(self):
        data = {'result': ['1', '2', {'3': [4, 5]}]}
        self.command.set_result(data)
        self.eq(self.command.pretty(),
                json.dumps(data, sort_keys=True, indent=4,
                           separators=(',', ': ')))

    def test_pretty_datetime(self):
        data = {'d': datetime.now()}
        self.command.set_result(data)
        self.eq(self.command.pretty(),
                '{\n    "d": "%s"\n}' % data['d'].isoformat(' '))