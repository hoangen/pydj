# Welcome to Python Dependency Injection Framework

I don't how this PyDJ framework will help, but let's give it a try.

### Set up

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run tests

`python -m unittest`

### Build

`python -m build`

### Install (optional)

`pip install --force-reinstall dist/pydj-0.0.1-py3-none-any.whl`

### Run

`python showcase.py`

And you will see:

```
running server at http://127.0.0.1:8085
happy coding...
```

## Stay tuned!

I'm doing it as fast as I can.

## Missing Features

- proxy object for method calls
- prototype scope
- circular dependency
- support @bean, @configuration annotation
- support REST annotation @rest, @get, @put, @post, @patch, @delete
