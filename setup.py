#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import dask_lsf



with open('README.rst') as readme_file:
    readme = readme_file.read()

version = dask_lsf.__version__

requirements = [
    'dask',
    'dask_jobqueue',
]

test_requirements = [ ]

setup(
    author="Akarshan Arora",
    author_email='akarshanarora@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="APIs to enable lsf jobs from python using dask",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords='dask_lsf, dask, lsf, EDA, VLSI',
    name='dask_lsf',
    packages=find_packages(include=['dask_lsf', 'dask_lsf.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/akarshanarora/dask_lsf',
    version=version,
    zip_safe=False,
)
