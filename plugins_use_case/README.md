Layout:
```
├── build_helper.py
├── core
│   └── __init__.py
├── plugins
│   └── p1
│       ├── build
│       │   └── bdist.linux-x86_64
│       ├── p1
│       │   └── __init__.py
│       └── setup.py
├── README.md
└── setup.py
```

Installation of plugin works in editable mode:
```
$ pip install -e plugins/p1/
Obtaining file:///home/omry/dev/test_pip/plugins_use_case/plugins/p1
Installing collected packages: plugin-p1
  Running setup.py develop for plugin-p1
Successfully installed plugin-p1
```

Trying a real installation fails because it's using things outside the source tree:
```
$ pip install plugins/p1/
Processing ./plugins/p1
    ERROR: Command errored out with exit status 1:
     command: /home/omry/miniconda3/envs/test-pip/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-req-build-t5nja8_7/setup.py'"'"'; __file__='"'"'/tmp/pip-req-build-t5nja8_7/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-et54elup
         cwd: /tmp/pip-req-build-t5nja8_7/
    Complete output (6 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-req-build-t5nja8_7/setup.py", line 8, in <module>
        from build_helper import get_version
    ModuleNotFoundError: No module named 'build_helper'
    Appending root locaiton to sys.path /
    ----------------------------------------
WARNING: Discarding file:///home/omry/dev/test_pip/plugins_use_case/plugins/p1. Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```