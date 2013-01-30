#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='control face',
      description='web interface for launching command',
      author='dsociative',
      author_email='admin@geektech.ru',
      packages=find_packages('control_face'),
      dependency_links = [
          "http://github.com/dsociative/ztest/tarball/master#egg=ztest",
          "http://github.com/dsociative/class_collector/tarball/master#egg=class_collector"
      ],
      install_requires=['flask', 'Flask-WTF', 'blinker',
                        'jinja2-highlight',
                        'ztest']
     )
