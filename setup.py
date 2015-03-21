"""Package setup configuration.

To Install package, run:
    >>> python setup.py install

To install package with a symlink, so that changes to the source files will be immediately available, run:
    >>> python setup.py develop

To run the tests:
    >>> python setup.py test

To upload the distribution:
    >>> python setup.py sdist upload
"""

from __future__ import print_function
from setuptools import setup, find_packages

__version__ = '0.1.1'

setup(
    name='mutabletuple.mutabletuple',
    version=__version__,
    description='Mutable tuple that behaves like dict with fixed keys.',
    long_description=open('README.txt').read() + '\n' + open('CHANGES.txt').read(),
    url='https://github.com/nicolasbessou/mutabletuple',
    include_package_data=True,
    author='Nicolas BESSOU',
    author_email='nicolas.bessou@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['namedlist'],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 ],
    test_suite='mutabletuple.tests',
    )
