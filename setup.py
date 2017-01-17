"""
test a
"""
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
        'b_test==1',
    ],
    dependency_links=[
        'git+https://github.com/benvand/b_test.git#egg=c_test-1'
    ],
    extras_require={
        'dev': ['ipython',]
    }


)
