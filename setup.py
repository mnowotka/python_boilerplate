#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mnowotka'

from setuptools import setup

setup(
    name='',
    version='0.0.2',
    entry_points={
        'console_scripts': [
            'some_script=...']
    },
    author='Michal Nowotka',
    author_email='mmmnow@gmail.com',
    description='...',
    url='https://github.com/mnowotka/...',
    license='MIT',
    packages=['...',
              ],
    long_description=open('README.md').read(),
    tests_require=['...'],
    install_requires=['...',],
    package_data={
        '...': ['samples/*', 'static/*', 'tests/*'],
        },
    include_package_data=False,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7'],
    zip_safe=False,
)
