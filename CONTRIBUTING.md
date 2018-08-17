Contributing
============

Setup
-----

```bash
git clone REPO
```

Test
----

Unit and integration tests:

```bash
python test_change_utils.py
```

Release
-------

  1. Update the file [CHANGELOG.md](CHANGELOG.md)
  2. Update the version in the file [\__init__.py](pysnow_change_epfl/__init__.py)
  3. Create the tag (``git tag -a <version> -m "Version <version>"``)
  4. Publish in [pypi.org](https://pypi.org/project/pysnow-change-epfl/):
```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

License
-------

Apache License 2.0

(c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2018.

See the [LICENSE](LICENSE) file for more details.
