# -*- coding: utf8 -*-

from flask import Flask, render_template, request, url_for, current_app, \
    Blueprint
from werkzeug.utils import redirect
from control_face.tests.test_env import test_config


class MyFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions',
        []).append('jinja2_highlight.HighlightExtension')



control_app = Blueprint('control_app', __name__, template_folder='templates')

def get_mapper():
    return current_app.config['MAPPER']


def init_command(command_name):
    return get_mapper()[command_name](request.form)


@control_app.route('/<command_name>',  methods=['GET', 'POST'])
def command(command_name):
    command = init_command(command_name)

    if request.method == 'POST' and command.form.validate():
        command.execute()

    return render_template('gate.html', command=command)


@control_app.route('/')
def list_command():
    return redirect(url_for('.command', command_name=get_mapper().keys()[0]))


def create_app(config):
    app = MyFlask(__name__)
    app.register_blueprint(control_app)
    app.config.from_object(config)
    return app

if __name__ == '__main__':
    app = create_app(test_config)
    app.run(debug=True)
