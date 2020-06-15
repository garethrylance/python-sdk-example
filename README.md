# python-sdk-example

Example of a pip installable python wrapper

## Installing

```
pip install
```

## Developing

1. Create a venv and activate if required

```powershell
python -m venv ./.venv
#enable python virtual environment
./.venv/bin/activate.ps1
```

2. Install dependancies

```powershell
# This install this module as symlinks to and all dependancies including the ones needed locally.
# It uses setup.py to find dependancies.
pip install -e  .[development] # This install this module as symlinks to and all dependancies including the ones needed locally.
```
