# -*- coding: utf-8 -*-
from setuptools import setup

APP=['konfig_dzila.py']

OPTIONS = {
    'argv_emulation': True,
}

setup(
      app=APP,
      options={'py2app': OPTIONS},
      setup_requires=['py2app']
)
