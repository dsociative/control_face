# -*- coding: utf8 -*-
from control_face.command import ControlCommand


class CommandSomethingElse(ControlCommand):

    name = 'something.else'

    def execute(self):
        self.set_result({'this': {'is': ['response', 'long']}})