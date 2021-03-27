# Exporting those as is to allow us to play the part of a build backend.
from setuptools.build_meta import build_sdist
from setuptools.build_meta import build_wheel

# Additional functions here will be available to setup.py
def get_version():
    return "1.0.3"


__all__ = [
    "build_sdist",
    "build_wheel",
    "get_version",
]
