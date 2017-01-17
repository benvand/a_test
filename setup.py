"""
test a
"""
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages


version='1'


setup(
    name='test_a',
    version='1',
    url='https://github.com/benvand/test_a',
    license='MIT',
    author='benvand',
    description='A',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'b_test',
    ],
    dependency_links=[
        'git+https://github.com/benvand/b_test.git'
    ],

)
