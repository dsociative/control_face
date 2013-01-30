#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='control face',
      description='web interface for launching command',
      author='dsociative',
      author_email='admin@geektech.ru',
      packages=find_packages(),
      include_package_data=True,
      dependency_links = [
          "http://github.com/dsociative/ztest/tarball/master#egg=ztest-0.0.0",
          "http://github.com/dsociative/class_collector/tarball/master#egg=class_collector-0.0.0"
      ],
      install_requires=['flask', 'Flask-WTF', 'blinker',
                        'jinja2-highlight',
                        'ztest']
     )
