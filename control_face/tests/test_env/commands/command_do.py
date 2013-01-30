# -*- coding: utf8 -*-
from wtforms import Form, TextField
from wtforms.validators import Required
from control_face.command import ControlCommand


class CommandDo(ControlCommand):

    name = 'command.do'

    class CommandForm(Form):
        what = TextField(validators=[Required()])

    def execute(self):
        self.set_result({'nothing': 'here'})