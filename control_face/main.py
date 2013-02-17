# -*- coding: utf8 -*-

from flask import Flask, render_template, request, url_for, current_app, \
    Blueprint, abort
from werkzeug.utils import redirect
from control_face.tests.test_env import test_config


class ControlApp(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions',
        []).append('jinja2_highlight.HighlightExtension')



control_app = Blueprint('control_app', __name__, template_folder='templates')

def get_mapper():
    return current_app.config['MAPPER']


def get_command(name):
    return get_mapper().get(name)


@control_app.route('/<name>',  methods=['GET', 'POST'])
def command(name):
    command_cls = get_command(name)
    if not command_cls:
        abort(404)
    command = command_cls(request.form)

    if request.method == 'POST' and command.form.validate():
        command.execute()

    return render_template('gate.html', command=command)


@control_app.route('/')
def list_command():
    return redirect(url_for('.command', name=get_mapper().keys()[0]))


def create_app(config):
    app = ControlApp(__name__)
    app.register_blueprint(control_app)
    app.config.from_object(config)
    return app

if __name__ == '__main__':
    app = create_app(test_config)
    app.run(debug=True)
