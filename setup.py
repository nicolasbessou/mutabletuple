"""Package setup configuration."""

from __future__ import print_function
from setuptools import setup

setup(
    name='mutabletuple',
    version='0.1',
    description='Mutable named tuple that behave like dict with fixed keys.',
    long_description=open('README.rst').read() + '\n' + open('CHANGES.rst').read(),
    url='http://github.com/????',
    author='Nicolas BESSOU',
    author_email='nicolas.bessou@gmail.com',
    license='MIT',
    packages=['mutabletuple'],
    install_requires=[
              'namedlist',
          ],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 ],
    test_suite='nose.collector',
    tests_require=['nose'],
    )
