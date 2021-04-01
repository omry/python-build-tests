Build command:
```
$ python setup.py sdist bdist_wheel
```

Content of sdist looks reasonable:
```
$ tar tzf dist/namespace_pkg_test-1.0.0.tar.gz 
namespace_pkg_test-1.0.0/
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

Content of wheel initially looks okay:
```
$ rm -rf build dist
$ python setup.py sdist bdist_wheel
...
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
Subsequent run contains build even though it's excluded in setup.cfg:
```
$ python setup.py sdist bdist_wheel
...
$ unzip -t dist/*.whl
Archive:  dist/namespace_pkg_test-1.0.0-py3-none-any.whl
    testing: build/lib/namespace_pkg/plugin1/__init__.py   OK
    testing: build/lib/namespace_pkg/plugin1/file.py   OK
    testing: namespace_pkg/plugin1/__init__.py   OK
    testing: namespace_pkg/plugin1/file.py   OK
    testing: namespace_pkg/plugin1/resource.yaml   OK
    testing: namespace_pkg_test-1.0.0.dist-info/METADATA   OK
    testing: namespace_pkg_test-1.0.0.dist-info/WHEEL   OK
    testing: namespace_pkg_test-1.0.0.dist-info/top_level.txt   OK
    testing: namespace_pkg_test-1.0.0.dist-info/RECORD   OK
No errors detected in compressed data of dist/namespace_pkg_test-1.0.0-py3-none-any.whl.
```