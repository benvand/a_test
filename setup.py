"""
test a
"""
from setuptools import setup, find_packages


version='1.0.0'


setup(
    name='a_test',
    version='1.0.0',
    url='https://github.com/benvand/a_test',
    license='MIT',
    author='benvand',
    description='A',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'b_test==1.0.0',
    ],
    dependency_links=[
        'git+https://github.com/benvand/b_test.git#egg=b_test-1.0.0'
    ],
    extras_require={
        'dev': ['pytz',]
    }


)
