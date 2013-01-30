# -*- coding: utf8 -*-
from contextlib import contextmanager
from flask import template_rendered, request
from wtforms import TextField
from class_collector import ClassCollector

from control_face.command import ControlCommand
from control_face.main import app
from control_face.tests.base_test import BaseTest


@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


class TestGateHandler(BaseTest):

    def setUp(self):
        self.client = app.test_client()
        self.mapper = ClassCollector('control_face/tests/test_env',
                                     ControlCommand).mapper()
        app.config['MAPPER'] = self.mapper
        app.config['TESTING'] = True

    def get_context(self, templates, name):
        template, context = templates[0]
        return context[name]

    def eq_context(self, templates, name, value):
        template, context = templates[0]
        self.eq(context[name], value)

    def test_index(self):
        rv = self.client.get('/')
        self.eq(rv.location, 'http://localhost/command.do')

    def test_command_do_form(self):
        with captured_templates(app) as templates:
            self.client.get('/command.do')
            command = self.get_context(templates, 'command')
            self.isinstance(command.form.what, TextField)

    def test_command_try_exec(self):
        with captured_templates(app) as templates:
            self.client.post('/something.else', data={'what': 'whatever'})
            command = self.get_context(templates, 'command')
            self.eq(command.result, {'this': {'is': ['response', 'long']}})