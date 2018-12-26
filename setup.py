"""SmartThings Cloud API"""
from setuptools import find_packages, setup
import pysmartapp

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name=pysmartapp.__title__,
      version=pysmartapp.__version__,
      description='A python library for building a SmartThings SmartApp',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/andrewsayre/pysmartapp',
      author='Andrew Sayre',
      author_email='andrew@sayre.net',
      license='MIT',
      packages=find_packages(),
      install_requires=['httpsig==1.3.0'],
      tests_require=['tox'],
      platforms=['any'],
      keywords=["smartthings","smartapp"],
      zip_safe=False,
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries",
          "Topic :: Home Automation",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          ])
