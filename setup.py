#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Pillow==9.0.1']

setup_requirements = [
    'pytest-runner',
]

test_requirements = ['pytest', 'pytest-mock']

setup(
    author="Wenjie Wu",
    author_email='wuwenjie718@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A simulator(based tk) for dotPack.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='dotpack',
    name='dotpack-tk',
    packages=['dotpack'],
    entry_points={
        'console_scripts': [
            # 'dotpack-scan = dotpack.tools.scan:scan',
        ],
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/longan-link/dotpack_pyclient',
    version='0.0.4',
    zip_safe=False,
)
