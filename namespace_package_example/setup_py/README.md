Build command:
```
$ python setup.py sdist bdist_wheel
```

Content of sdist.
As desired, contains both code and resources from namespace_pkg/plugin1, in addition to the tests:
```
$ tar tzf dist/namespace_pkg_test-1.0.0.tar.gz 
namespace_pkg_test-1.0.0/
namespace_pkg_test-1.0.0/MANIFEST.in
namespace_pkg_test-1.0.0/PKG-INFO
namespace_pkg_test-1.0.0/README.md
namespace_pkg_test-1.0.0/namespace_pkg/
namespace_pkg_test-1.0.0/namespace_pkg/plugin1/
namespace_pkg_test-1.0.0/namespace_pkg/plugin1/__init__.py
namespace_pkg_test-1.0.0/namespace_pkg/plugin1/file.py
namespace_pkg_test-1.0.0/namespace_pkg/plugin1/resource.yaml
namespace_pkg_test-1.0.0/namespace_pkg_test.egg-info/
namespace_pkg_test-1.0.0/namespace_pkg_test.egg-info/PKG-INFO
namespace_pkg_test-1.0.0/namespace_pkg_test.egg-info/SOURCES.txt
namespace_pkg_test-1.0.0/namespace_pkg_test.egg-info/dependency_links.txt
namespace_pkg_test-1.0.0/namespace_pkg_test.egg-info/top_level.txt
namespace_pkg_test-1.0.0/setup.cfg
namespace_pkg_test-1.0.0/setup.py
namespace_pkg_test-1.0.0/tests/
namespace_pkg_test-1.0.0/tests/test_foo.py
```

Content of wheel.
As desired, contains only both code and resources from namespace_pkg/plugin1: 
```
$ unzip -t dist/*.whl
Archive:  dist/namespace_pkg_test-1.0.0-py3-none-any.whl
    testing: namespace_pkg/plugin1/__init__.py   OK
    testing: namespace_pkg/plugin1/file.py   OK
    testing: namespace_pkg/plugin1/resource.yaml   OK
    testing: namespace_pkg_test-1.0.0.dist-info/METADATA   OK
    testing: namespace_pkg_test-1.0.0.dist-info/WHEEL   OK
    testing: namespace_pkg_test-1.0.0.dist-info/top_level.txt   OK
    testing: namespace_pkg_test-1.0.0.dist-info/RECORD   OK
No errors detected in compressed data of dist/namespace_pkg_test-1.0.0-py3-none-any.whl.
```