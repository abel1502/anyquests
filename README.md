# Anyquests

**Anyquests** is a transparent wrapper around either [requests](https://github.com/psf/requests)
or [niquests](https://github.com/jawah/niquests) which doesn't install either automatically.

## Motivation

Niquests is a fork of requests made to address important flaws and support
modern web features. However, to do this niquests depends on [urllib3.future](https://github.com/jawah/urllib3.future),
which takes a dramatic approach to backwards compatibility by shadowing
the original [urllib3](https://github.com/urllib3/urllib3) if it is present.
While this can be disabled during installation, a package including urllib3.future
as a dependency (even transitive) cannot control this behavior. The potential
of silently breaking users' installations can discourage them from depending on
niquests. This package is meant to address this issue.

Rather than depending on one or the other, package authors can depend on anyquests
and let the end user decide which library to install. Anyquests will pick
whichever is available, prioritizing niquests.

## Usage

Add `anyquests` to the dependencies in your `pyproject.toml`. Then just import
the library with:

```python
import anyquests
# or
import anyquests as requests
```

The imported library will be the same as the result of either `import niquests`
or `import requests`. If none are availabe, an `ImportError` will be raised
with a helpful message instructing the user to install one or the other.

If you want to guarantee that your package will run out of the box even if the
user doesn't have either `requests` or `niquests` installed, you can also
add an explicit dependency on `requests`. `anyquests` will still opportunistically
switch to `niquests` when available.

Note that this package does not impose any restrictions on the versions of
either `requests` or `niquests`.

## License

To match the licenses of the original requests and niquests, this package is
licensed under the Apache License, Version 2.0.

© 2026 abel1502
