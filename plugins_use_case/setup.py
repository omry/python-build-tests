import setuptools
from os.path import dirname
from build_helper import get_version

setuptools.setup(
    name="core",
    version=get_version(dirname(__file__), "core", "__init__.py"),
)
