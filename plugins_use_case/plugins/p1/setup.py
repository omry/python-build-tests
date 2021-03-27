import sys
from os.path import dirname, abspath
root_location = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(root_location)

import setuptools
from build_helper import get_version

setuptools.setup(
    name="plugin_p1",
    version=get_version(dirname(__file__), "p1", "__init__.py"),
)
