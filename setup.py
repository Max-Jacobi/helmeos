from setuptools import setup
import subprocess
import sys
from os import chdir
from distutils.command.build_py import build_py


setup(
    name="helmeos",
    version="1.0dev",
    author="Matt Coleman",
    author_email="msbc@astro.princeton.edu",
    packages=["helmeos"],
    description="A Python implementation/port of Frank Timmes' Helmholtz EoS.",
)
