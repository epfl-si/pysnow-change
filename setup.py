# -*- coding:utf-8 -*-

"""
(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018-2019.
"""

from setuptools import setup
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysnow_change_epfl',
    version=__import__('pysnow_change_epfl').__version__,
    description='ServiceNow change creation tool for EPFL-IDevelop',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/epfl-idevelop/pysnow-change',

    author='Olivier Bieler',
    author_email='olivier.bieler@epfl.ch',

    license="Apache License 2.0",
    install_requires=[
        'requests>=2.21.0,<3.0',
        'lxml>=3.7.3,<4.0',
        'zeep>=2.5.0,<3.0',
    ],
    packages=['pysnow_change_epfl'],
    zip_safe=False
)
