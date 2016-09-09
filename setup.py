#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    name='kibitzer',
    version='1.2.5',
    description="Self hosted web page changes monitoring",
    long_description=readme + '\n\n' + history,
    author="Peter Demin",
    author_email='peterdemin@gmail.com',
    url='https://github.com/peterdemin/kibitzer',
    packages=[
        'kibitzer',
    ],
    package_dir={
        'kibitzer': 'kibitzer',
    },
    entry_points={
        'console_scripts': [
            'kibitzer=kibitzer.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=[
        'Click>=6.0',
        'requests',
        'schedule',
        'sh',
        'pyyaml',
        'selenium',
        'xvfbwrapper',
        'bs4',
        'six',
    ],
    license="MIT license",
    zip_safe=False,
    keywords='kibitzer',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-pep8',
        'pylint',
        'mock',
        'pytest-mock',
    ],
)
