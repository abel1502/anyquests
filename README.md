# Anyquests

![PyPI - Version](https://img.shields.io/pypi/v/anyquests)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/anyquests)
![PyPI - License](https://img.shields.io/pypi/l/anyquests)

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

## I am an end user, which one to choose?

If you don't have any personal preference yet, choose `niquests`. `niquests` is
a fork of `requests` which supports newer features such as HTTP/3 over QUIC.
Be aware, however, that by default installing `niquests` will shadow `urllib3`
with a different, improved implementation.
If this is a concern for you, see https://niquests.readthedocs.io/en/latest/community/faq.html#cohabitation
for instructions on how to disable that. See also https://niquests.readthedocs.io/en/latest/community/faq.html#what-is-urllib3-future
for an explanation of why `niquests` does that.

## Usage

Add `anyquests` to the dependencies in your `pyproject.toml`, for example by running:

```shell
uv add anyquests
```

Then just import the library with:

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

### Typing

By default a type checker cannot know the members of `anyquests` or their types.
This can be addressed with separate type stubs, but this would create tight coupling
to specific versions of `requests` and `niquests`. Instead, since `niquests`
promises to maintain full backwards compatibility with `requests`, the
recommended solution is to:

1. Include `anyquests` and `requests` as dependencies in your `pyproject.toml`.
2. Include the following among your imports:
   
   ```python
   from typing import TYPE_CHECKING

   import anyquests
   if TYPE_CHECKING:
       import requests as anyquests
   ```
   
   Alternatively, if you prefer using the name `requests`, include:
   
   ```python
   from typing import TYPE_CHECKING

   import anyquests as requests
   if TYPE_CHECKING:
       import requests
   ```

## Implementation

This package consists of just [25 lines of code](./src/anyquests/__init__.py),
including empty lines and a multiline error message. It attempts
to import `niquests`, then in case of failure, attempts to import
`requests`, then in case of another failure raises an `ImportError`
with an explanation and instructions. If an import succeeds, the
`anyquests` module is fully substituted for the imported module,
which maintains maximum compatibility and ensures no overhead.

If you believe you found an issue, or have an idea on how to improve
this package, feel free to [open an issue](https://github.com/abel1502/anyquests/issues).

## License

To match the licenses of the original requests and niquests, this package is
licensed under the Apache License, Version 2.0.

© 2026 abel1502
