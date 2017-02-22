from setuptools import setup

import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name="{{cookiecutter.module}}",
      use_scm_version=True,
      setup_requires=['setuptools_scm'] + pytest_runner,
      tests_require=['pytest', 'pytest-cov'],
      packages=['{{cookiecutter.module}}'])