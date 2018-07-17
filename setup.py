# -*- coding:utf-8 -*-

"""
(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.
"""

from setuptools import setup

setup(
    name='pysnow_change_epfl',
    version=__import__('pysnow_change_epfl').__version__,
    description='ServiceNow change creation tool for EPFL-IDevelop',
    long_description=open('README.md', 'r').read(),

    url='https://github.com/epfl-idevelop/pysnow-change',

    author='Olivier Bieler',
    author_email='olivier.bieler@epfl.ch',

    license="Apache License 2.0"
    install_requires=[
        'lxml==3.7.3',
        'zeep==2.5.0',
    ],
    packages=['pysnow_change_epfl'],
    zip_safe=False
)
