Structure:
```
$ tree
.
├── build_helper
│   ├── build_helper
│   │   └── __init__.py
│   └── setup.py
├── example
│   └── __init__.py
├── README.md
└── setup.py
```

Installing build_helper:
```
$ pip install build_helper/
Processing ./build_helper
Building wheels for collected packages: build-helper
  Building wheel for build-helper (setup.py) ... done
  Created wheel for build-helper: filename=build_helper-0.0.0-py3-none-any.whl size=1261 sha256=aa0ee67ef3385cba13e32659fb3635047631d0466ef0861c71badd5d3d67f7fd
  Stored in directory: /tmp/pip-ephem-wheel-cache-_dpz2jwm/wheels/36/26/ae/14e3035420d431e16878ed266d823b24627dc0fe56af0b53b3
Successfully built build-helper
Installing collected packages: build-helper
  Attempting uninstall: build-helper
    Found existing installation: build-helper 0.0.0
    Uninstalling build-helper-0.0.0:
      Successfully uninstalled build-helper-0.0.0
Successfully installed build-helper-0.0.0
```

Successfully installing primary project:
```
$ pip install .
Processing /home/omry/dev/test_pip
Building wheels for collected packages: example
  Building wheel for example (setup.py) ... done
  Created wheel for example: filename=example-1.0.3-py3-none-any.whl size=991 sha256=21a95c7e50946865cb6f4565842e455ab9a972ceae1800e534d391e2032286c0
  Stored in directory: /tmp/pip-ephem-wheel-cache-k02av0q_/wheels/57/c2/45/2447e9fc2acaa90e70563527f393553ccc1297fb8d529f0c92
Successfully built example
Installing collected packages: example
  Attempting uninstall: example
    Found existing installation: example 1.0.3
    Uninstalling example-1.0.3:
      Successfully uninstalled example-1.0.3
Successfully installed example-1.0.3
```

Creating an empty pyproject.yaml, after which installation fails:
```
$ touch pyproject.toml
$ pip install .
Processing /home/omry/dev/test_pip
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  ERROR: Command errored out with exit status 1:
   command: /home/omry/miniconda3/envs/test-pip/bin/python /home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py get_requires_for_build_wheel /tmp/tmpybcsa03y
       cwd: /tmp/pip-req-build-_31oxf1l
  Complete output (18 lines):
  Traceback (most recent call last):
    File "/home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py", line 280, in <module>
      main()
    File "/home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py", line 263, in main
      json_out['return_val'] = hook(**hook_input['kwargs'])
    File "/home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py", line 114, in get_requires_for_build_wheel
      return hook(config_settings)
    File "/tmp/pip-build-env-m265pb85/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 154, in get_requires_for_build_wheel
      return self._get_build_requires(
    File "/tmp/pip-build-env-m265pb85/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 135, in _get_build_requires
      self.run_setup()
    File "/tmp/pip-build-env-m265pb85/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 258, in run_setup
      super(_BuildMetaLegacyBackend,
    File "/tmp/pip-build-env-m265pb85/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 150, in run_setup
      exec(compile(code, __file__, 'exec'), locals())
    File "setup.py", line 3, in <module>
      from build_helper import get_version
  ImportError: cannot import name 'get_version' from 'build_helper' (unknown location)
  ----------------------------------------
WARNING: Discarding file:///home/omry/dev/test_pip. Command errored out with exit status 1: /home/omry/miniconda3/envs/test-pip/bin/python /home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py get_requires_for_build_wheel /tmp/tmpybcsa03y Check the logs for full command output.
ERROR: Command errored out with exit status 1: /home/omry/miniconda3/envs/test-pip/bin/python /home/omry/miniconda3/envs/test-pip/lib/python3.8/site-packages/pip/_vendor/pep517/_in_process.py get_requires_for_build_wheel /tmp/tmpybcsa03y Check the logs for full command output.
```
