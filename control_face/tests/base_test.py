# -*- coding: utf8 -*-
from ztest import ZTest
from control_face.main import create_app
from control_face.tests.test_env.test_config import TestConfig


test_app = create_app(TestConfig())

class BaseTest(ZTest):
    pass