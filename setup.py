import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    return open(os.path.join(os.path.dirname(__file__), 'version')).read()


setup(
    name='stararchiver',
    version=get_version(),
    scripts=['stararchiver'],
    long_description=read('README.md'),
    license='MIT',
    keywords = "github stars archiver",
    packages=find_packages(),
    data_files=['version'],
    include_package_data=True,
    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
