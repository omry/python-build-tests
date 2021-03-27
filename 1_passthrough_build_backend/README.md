layout:
```
$ tree
.
├── build-tools    # NOT a pythonpath root.
│   └── build_helper
│       └── __init__.py
├── example
│   └── __init__.py
├── pyproject.toml
├── README.md
└── setup.py
```

`pyproject.toml`:
```toml
[build-system]
requires = ["setuptools", "wheel"] 
backend-path = ["build-tools"]
build-backend = "build_helper"
```

`build-tools/build_helper/__init__.py`:
```python
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
```
Installing works as expected:
```shell
$ pip install .
Processing /home/omry/dev/test_pip/1_passthrough_build_backend
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Building wheels for collected packages: example
  Building wheel for example (PEP 517) ... done
  Created wheel for example: filename=example-1.0.3-py3-none-any.whl size=991 sha256=653837cc22d9faefe0377bd101c233bc31f727713848fff1190b36ae4b91ef2d
  Stored in directory: /tmp/pip-ephem-wheel-cache-lgg4nrlw/wheels/9b/0f/72/318c99afc80cfa4dfa9ad7c4466cad446b6bc1405e4ef5c7fe
Successfully built example
Installing collected packages: example
Successfully installed example-1.0.3
```
