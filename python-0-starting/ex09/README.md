## Build

```
python setup.py sdist bdist_wheel
(for setup.py)
        or
python -m build
(for pyproject.toml)
```

## Install

```
pip3 install ./dist/ft_package-0.0.1.tar.gz
```

## Display

```
pip3 show -v ft_package
```

## Test

```
python3.10 tester.py
```

## Uninstall

```
pip3 uninstall ft_package
```