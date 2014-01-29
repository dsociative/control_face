# -*- coding: utf8 -*-

from flask import Flask, render_template, request, url_for, current_app, \
    Blueprint, abort
from werkzeug.utils import redirect


class ControlApp(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions',
        []).append('jinja2_highlight.HighlightExtension')


control_app = Blueprint('control_app', __name__, template_folder='templates')


def get_mapper():
    return current_app.config['MAPPER']


def get_command_names():
    return current_app.config['COMMAND_NAMES']


def get_command(name):
    return get_mapper().get(name)


def command(name):
    command_cls = get_command(name)
    if not command_cls:
        abort(404)
    command = command_cls(request.form)

    if request.method == 'POST' and command.form.validate():
        command.execute()

    return render_template('gate.html', command=command)


def list_command():
    return redirect(url_for('.command', name=get_command_names()[0]))


def routes(app):
    root_url = app.config['ROOT_URL']
    app.add_url_rule('%s/' % root_url, 'index', list_command)
    app.add_url_rule(
        '%s/<name>' % root_url, 'command', command, methods=['GET', 'POST']
    )


def configure(app, config):
    app.config.from_object(config)
    app.config.setdefault('COMMAND_NAMES', sorted(app.config['MAPPER'].keys()))
    app.config.setdefault('ROOT_URL', '')


def create_app(config):
    app = ControlApp(__name__)
    app.register_blueprint(control_app)
    configure(app, config)
    routes(app)
    return app

if __name__ == '__main__':
    from control_face.tests.test_env import test_config
    app = create_app(test_config)
    app.run(debug=True)
