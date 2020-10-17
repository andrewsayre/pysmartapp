"""SmartThings Cloud API"""
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join("README.md"), 'r') as fh:
    long_description = fh.read()

consts = {}
with open(os.path.join('pysmartapp', 'const.py'), 'r') as fp:
    exec(fp.read(), consts)

setup(name=consts['__title__'],
      version=consts['__version__'],
      description='A python library for building a SmartThings SmartApp',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/andrewsayre/pysmartapp',
      author='Andrew Sayre',
      author_email='andrew@sayre.net',
      license='MIT',
      packages=find_packages(exclude=('tests*',)),
      install_requires=['httpsig>=1.3.0,<2.0.0'],
      tests_require=['tox>=3.5.0,<4.0.0'],
      platforms=['any'],
      keywords=["smartthings", "smartapp"],
      zip_safe=False,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries",
          "Topic :: Home Automation",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          ])
