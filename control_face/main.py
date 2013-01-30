# -*- coding: utf8 -*-

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from control_face.tests.test_env import test_config


class MyFlask(Flask):
    jinja_options = dict(Flask.jinja_options)
    jinja_options.setdefault('extensions',
        []).append('jinja2_highlight.HighlightExtension')

app = MyFlask(__name__)


def get_mapper():
    return app.config['MAPPER']


def init_command(command_name):
    return get_mapper()[command_name](request.form)


@app.route('/<command_name>',  methods=['GET', 'POST'])
def command(command_name):
    command = init_command(command_name)

    if request.method == 'POST' and command.form.validate():
        command.execute()

    return render_template('gate.html', command=command)


@app.route('/')
def list_command():
    return redirect(url_for('command', command_name=get_mapper().keys()[0]))


if __name__ == '__main__':
    app.config.from_object(test_config)
    app.run(debug=True)
