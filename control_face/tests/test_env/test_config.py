# -*- coding: utf8 -*-
from os import path
from class_collector import ClassCollector
from control_face.command import ControlCommand


MAPPER = ClassCollector(path.join(path.dirname(__file__), 'commands'),
                        ControlCommand).mapper()
PROJECT_NAME = 'Test'
