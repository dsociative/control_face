# -*- coding: utf8 -*-
from ztest import ZTest
from control_face.main import create_app
from control_face.tests.test_env import test_config


test_app = create_app(test_config)

class BaseTest(ZTest):
    pass