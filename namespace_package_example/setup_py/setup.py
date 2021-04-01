# [options.package_data]
# namespace_pkg = *.yaml

from setuptools import setup, find_namespace_packages
from read_version import read_version

setup(
    name="namespace_pkg_test",
    version=read_version("namespace_pkg", "plugin1", "__init__.py"),
    packages=find_namespace_packages(include=["namespace_pkg.*"]),
    include_package_data=True,
)
