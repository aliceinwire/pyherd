import sys, os

from setuptools import setup, find_packages

import pyherd

long_description = open('README.md').read()


setup_args = dict(
    name="pyherd",
    version=pyherd.__version__,
    description='Python herd parsing command-line tool',
    long_description=long_description,
    author="Alice Ferrazzi",
    author_email="alice.ferrazzi@gmail.com",
    download_url="https://github.com/aliceinwire/pyherd/archive/master.zip",
    url="https://github.com/aliceinwire/pyherd.git",
    license="Python Software Foundation License",
    keywords="Python herd parsing command-line tool",
    platforms="gentoo",
    classifiers="""\
Development Status :: 5 - Production/Stable
Environment :: Console
Intended Audience :: Developers
License :: OSI Approved :: Python Software Foundation License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development""".splitlines(),
    py_modules=['pyherd'],
)

if __name__ == '__main__':
    setup(**setup_args)

