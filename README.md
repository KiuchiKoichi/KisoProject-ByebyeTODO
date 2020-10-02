# KisoProject-ByebyeTODO
Bye bye TODO

## refs
* [このサイト](https://qiita.com/ragnar1904/items/defab259cde73669cc6d) を参考にディレクトリを構成

## flake8
### features
* if there has error, your coding is wrong.
### usage
```
flake8 .
```

## mypy
### features
* must write __type annotation__
    * especially Parameters & Returns
* must write docstrings
### usage
```
mypy .
```

## configuration
```
.
├── account
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── poetry.lock
└── pyproject.toml
```
