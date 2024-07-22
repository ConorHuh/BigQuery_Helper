from setuptools import setup, find_packages
from version import __version__ as version

setup(name='bq_helper',
      packages=find_packages(include=['bq_helper', 'test_helper']),
      version=version,
      description='Helper class to simplify common read-only BigQuery tasks.',
      author='Conor Huh',
      url='https://github.com/ConorHuh/BigQuery_Helper',
      license='Apache 2.0',
      install_requires=['pandas', 'google-cloud-bigquery'],
      classifiers=['Programming Language :: Python :: 3'],
      )
