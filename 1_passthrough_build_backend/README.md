```layout
$ tree
.
├── build_helper
│   └── __init__.py
├── example
│   └── __init__.py
├── pyproject.toml
├── README.md
└── setup.py
```

pyproject.toml
```toml
[build-system]
requires = ["setuptools", "wheel"] 
backend-path = ["."]
build-backend = "build_helper"
```