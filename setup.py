from setuptools import setup, find_packages

with open('a_test_pkg/VERSION', 'r') as f:
    VERSION = f.readlines()[0].strip()

setup(
    version=VERSION,  # version set by tag
    packages=find_packages(exclude=['docs', 'tests', 'tests.*']),
)
