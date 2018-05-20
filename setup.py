import os
import re

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    rsa_source = open(
        os.path.join(os.path.dirname(__file__), 'stararchiver')
    ).read()
    version = re.search(
        r"^SA_VERSION = ['\"]([^'\"]*)['\"]",
        rsa_source,
        re.M,
    ).group(1)
    if not version:
        raise RuntimeError('Cannot find stararchiver version')
    return version


setup(
    name='stararchiver',
    python_requires='>=2.6, <3',
    version=get_version(),
    scripts=['stararchiver'],
    packages=find_packages(),
    install_requires=[
        'GitPython>=2.1.9',
        'requests>=2.18.4',
    ],
    long_description=read('README.md'),
    license='MIT',
    keywords = "github stars archiver",
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
