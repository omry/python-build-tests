# Not changing this one, so just import it and re-export it unchanged
from setuptools.build_meta import build_sdist
from setuptools.build_meta import build_wheel as orig_build_wheel


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    return orig_build_wheel(wheel_directory, config_settings, metadata_directory)


def get_version():
    return "1.0.3"


__all__ = [
    "build_sdist",
    "build_wheel",
    "get_version",
]
