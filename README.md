# KisoProject-ByebyeTODO
Bye bye TODO
pushのテスト

## refs
* [このサイト](https://qiita.com/__init__/items/b8fd530f3b8603231b35) を参考にディレクトリを構成
    * [ここから](https://qiita.com/__init__/items/b8fd530f3b8603231b35#%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8%E3%81%AE%E5%AE%9F%E8%A3%85) 未着手

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
