### 1_passthrough_build_backend

The Simplest approach, use a dummy build backend that delegates to setuptools.build_meta.* and add additional
logic available during build.

### plugins_use_case

A somewhat realistic emulation of the real problem.