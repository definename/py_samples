Python [Workshop](https://legacy.python.org/doc/essays/ppt/acm-ws/tsld001.htm) by Guido Van Rossum

Different [sorting](https://github.com/gwtw/py-sorting) algorithms implementation with python

> [Pip](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/pip.html) is a package manager + [Virtualenv](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/) is an environment manager = [Conda](https://conda.io/en/latest/) is both

> Linting analyzes how the code runs and detects errors whereas formatting simply restructures how code appears.

# Table of contents

## IDE and tools
- [Visual Studio Code](#visual-studio-code)
    - [Configure interpreter](#configure-interpreter)
    - [Configure and run debugger](#configure-and-run-debugger)
    - [Formatting](#formatting)
    - [Linting](#linting)
    - [Unit testing](#unit-testing)
    - [CTags](#ctags)
    - [Log Viewer](#log-viewer)
- [Anaconda](#anaconda)
## Language references
- [Operations](#operations)
- [Numbers](#numbers)
- [Strings](#strings)
- [Containers](#containers)
    - [Generators](#generators)
- [Function](#function)
- [Concepts](#concepts)
- [Module](#module)
- [Package](#package)
- [Class](#class)
- [Namespace](#namespace)
- [Format](#format)
- [Regex](#regex)
- [Serialization](#serialization)
- [Databases](#databases)
- [WWW](#www)
- [System](#system)
- [Concurrency](#concurrency)
- [RPC](#rpc)
## Library references
- [Random](#random)
- [pydoc](#pydoc)
## GUI
- [tkinter](#tkinter)
## Cloud
- [AWS IoT](#aws-iot)

---

# [Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)

## Configure interpreter

- Install `python` extention
- Select `python` interpreter
    - ctrl+shift+p
    - type `python: select interpreter`
    - select `python` interpreter from the list of available interpreters

As result `.vscode` folder will be created with `settings.json` file.  Inside of `setting.json` file `python.pythonPath` variable will point to the `python` interpreter.

## Configure and run debugger

- Set breakpoint
- ctrl+shift+d (go to debugging tab)
- Select `python: current file`
- Run debugging by pressing `F5`

## General settings

Disable minimap, render white spaces etc.:
```
    "files.associations": {
        "*.py": "python",
        "*.c": "c",
        "*.h": "c"
    },
    "editor.minimap.enabled": false,
    "editor.renderWhitespace": "all"
```

## Formatting

[autopep8](https://pypi.org/project/autopep8/) - autopep8 automatically formats Python code to conform to the PEP 8 style guide.

- Install `autopep8`: `sudo pip3 install autopep8`
- Retrive `autopep8` path: `which autopep8`
- `autopep8` path should be put in config section: `"python.formatting.autopep8Path":"<autopep8path>"`

Autoformatting workspace settings:
```
    "[python]":
    {
        "editor.formatOnSave": true,
    },
    "python.formatting.provider": "autopep8",
    "python.formatting.autopep8Path": "<autopep8path>",
    "python.formatting.autopep8Args": [
        "--max-line-length",
        "100"
    ]
```

## Linting

By default `VS Code` uses [pylint](https://www.pylint.org/) to provide linting support.

## Unit testing

The Python extension supports unit testing with Python's built-in `unittest` framework as well as `pytest` and `Nose`.

```
    "python.testing.unittestEnabled": true,
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        "./py_test",
        "-p",
        "test_*.py"
    ],
    "python.testing.pyTestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
    "python.testing.promptToConfigure": false
```

## CTags

Install [ctags](http://ctags.sourceforge.net/) and run: `ctags -R  --verbose=yes --append=yes --totals=yes .`

With `Ctrl+T` you will be able to use `ctags` functionality.

## Log Viewer

[Log viewer](https://gitlab.com/berublan/vscode-log-viewer) is extention to monitor text log files.

```
    "logViewer.watch": [
        {
            "title": "TextLog",
            "pattern": "/home/x/text.log"
        }
    ],
    "logViewer.options":
    {
        "fileCheckInterval":100,
        "encoding":"utf8"
    }
```

---

# [Anaconda](https://www.anaconda.com/):

Update `anaconda` from older version:
```
conda update conda
conda update anaconda
```

Lists available environments:

```
conda info --envs
```

Switch to particular environment:

```
conda activate custom
```

Search for particular package

```
conda search spyder
```

Install specific package into specific environment (by default package is installed into active environment):

```
conda install --name custom spyder=3.3.3
```

[Uninstall](https://docs.anaconda.com/anaconda/install/uninstall/) `anaconda`:

Install clean up tool:
```
conda install anaconda-clean
```

Remove all Anaconda-related files and directories without being prompted to delete each one
```
anaconda-clean --yes
```

On `Windows` remove `anaconda` with `Control Panel`. On `Linux` with command `rm -rf ~/anaconda`

---

# [jupyter nbviewer](https://nbviewer.jupyter.org/)

Create `*.ipynb` file and share it via `nbviewer` service

---

# Language references

## Operations

- `==` проверяет, равны ли значения объектов. 
- `is` проверяет идентичность объектов. Он возвращает значение True, только если оба имени ссылаются на один и тот же объект.

## Numbers

- Целые числа `1, 23, 3`
- Вещественные числа `1.1, 123.003`
- Числа фиксированной точности, see [decimal](https://docs.python.org/3/library/decimal.html) module
- Рациональные числа `1/2, 1/4 etc.` see [fractions](https://docs.python.org/3/library/decimal.html) module
- Множества `set([1, 2, 3])`, see [set](https://docs.python.org/3/library/stdtypes.html#set)
- Логические значения `True(1), False(0)`
- Целые числа неограниченной точности `9999999999999999999999999999999999999999999999`

## Strings

- Неформатированные строки
```
open(r"C:\new\text.dat", "w")
```

- Блочная строка
```
"""
Always look
on the bright
side of life.
"""
```

## Containers

- `Изменяемый` контейнер

`list`(Список) - `[1, 2, 3, "one", "two", "three"]`

> `list` представляют собой упорядоченные по позициям коллекции объектов произвольних типов
> и могут иметь неограниченное число уровней вложенности.

`dict`(Словарь) - `{ "seconds": "1", "minutes": "2", "hour": "3", "day": "4", "month": "5", "year": "5" }`
> `dict` представляет собой структуру данных вида: `ключ`: `значение`, элементы в словарях
> сохраняются по ключам, а не по позициям.

`set`(Множество) - `{1, 2, 3, 4, 5, 6, 0}`
> `set` позволяет решить задачу получения уникальных элементов

- `Неизменяемый` контейнер(только на первом уровне)

`tuple`(Кортеж) - `(1, 2, 3, 4, 5)`
>  Если в `tuple` добавить `list` его можно будет изменить

`frozenset`(Фиксированное множество) ???

### Generators

> Генераторы - это способ построить контейнер, применяя выражение к каждому элементу последовательности.

- `list` generator:
`l = [c * 2 for c in "SPAM"]`

- `dict` generator:
`d = {k: k*2 for k in "SPAM"}`

## Function

> `Функция` - это именованый фрагмент кода, отделенный от других.

`def` - Это инструкция. Когда интерпретатор достигает инструкции `def` и выполняет её, он создает новый обьект функции, в который упакует програмный код функции и свяжет объект с именем.

## Concepts

:point_up: `Присваивание` - в языке Python означает передача ссылок на объекты, которые фактически реализованы в виде указателей. В зависимости от того переданный объект относится к категории `mutable` либо `immutable` изменения будут видны либо не видны из вне.

:point_up: `Полиморфизс` - означает что смысл операции либо вызова зависит от типа обрабатываемого объекта.

:point_up: `Включение` — это компактный способ создать структуру данных из одного или более итераторов.

```
list - [ выражение for элемент in итерабельный объект ]
dict - { выражение_ключа: выражение_значения for выражение in итерабельный объект }
set - { выражение for выражение in итерабельный объект }
```

:point_up: `Замыкание` — это функция, которая динамически генерируется другой функцией, и они обе могут изменяться и запоминать значения переменных, которые были созданы вне функции.

:point_up: В Python `лямбда-функция` — это анонимная функция, выраженная одним выражением.

:point_up: В Python `генератор` — это объект, который предназначен для создания последовательностей.

:point_up: `Декоратор` — это функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию.

:point_up: `Пространства имен` — разделы, внутри которых определенное имя уникально и не связано с такими же именами в других пространствах имен.

:point_up: В Python используются `исключения`: код, который выполняется, когда происходит связанная с ним ошибка.

## Module

:point_up: `Модуль` — это всего лишь файл, содержащий код Python

> Eсли вы знакомы с книгой Gamma E. Design Patterns: Elements of Reusable Object-Oriented Software, можете использовать модули в Python как синглтоны

To create python module it is enough to create file `modulename.py`

In order to import python `module` we need to do the following: `import modulename`
It is also possible to import module and create alias for it in this way: `import modulename as mn`

To be able to import only specific function from python module we need to do the following: `from modulename import functionname`
To do the same with alias: `from modulename import functionname as fn`

## Package

:point_up: Модули организованные в иерархии файлов называются `пакетами`

In order to create `python` package we need to create directory and put all `*.py` files into that folder. Also `__init__.py` file should be created inside that folder to tell python is it should interpret that folder as package.

## Class

:point_up: `наследование` - создание нового класса из уже существующего, который при этом содержит какие-то дополнения и изменения

:point_up: `атрибуты` - иногда их называют информацией о состоянии

В Python *геттеры* и *сеттеры* не нужны, поскольку все атрибуты и методы являются открытыми, а от вас ожидается примерное поведение!

In order to make class attributes private we need to decorate their names with `__` e.g `__name`

:point_up: `полиморфизм` - это значит, что одна операция может быть произведена над разными объектами независимо от их класса.

:point_up: `объект` - это область памяти со значениями и ассоциированными с ними наборами операций.

:point_up: `динамическая типизация` - типы данных определяются автоматически и их не требуется объявлять в программном коде.

## Namespace

It works according to the given rule - `LEGB`

## Data

:point_up: `cтроки` — последовательности символов в кодировке Unicode, используемые для представления текстовых данных.

:point_up: `байты и массивы байтов` — последовательности восьмибитных целых чисел, используемые для представления двоичных данных.

:point_up: `unicode` — это действующий международный стандарт, определяющий символы всех языков мира плюс математические и другие символы.

:point_up: `UTF-8` — динамическую схему кодирования, oна использует для символа Unicode от одного до четырех байтов.

## Format

Python предлагает два способа форматирования строк, их часто называют `старым` стилем и `новым` стилем.

:point_up: Старый стиль форматирования строк имеет форму `строка % данные`

:point_up: Новый стиль форматирования имеет формат `'{} {} {}'.format(a, b, c)`

## Regex

`.` - любой символ

`*` - любое количество предыдущих елементов

`.*` - любое количество символов (даже ноль)

`?` - ноль или одно включение (опциональный символ)

`\b` - граница слова: `<граница слова>fish<граница слова>` -> `\bfish\b`

## Serialization

Сохранение структур данных в файл называется `сериализацией`

Library to serialize data as binary:

- [msgpack](https://msgpack.org/)
- [protobuf](https://github.com/protocolbuffers/protobuf)
- [avro](http://avro.apache.org/docs/current/)
- [thrift](http://thrift.apache.org/)

Поскольку они бинарные, ни один из них не может быть изменен человеком, вооружившимся текстовым редактором.

[HDF5](http://www.hdfgroup.org/why_hdf) — это бинарный формат данных, предназначенный для хранения многомерных или иерархических числовых данных.

## Databases

### Relational Database

> Relational Databases (pеляционная база данных) представляет собой множество взаимосвязанных таблиц, каждая из которых содержит информацию об объектах определенного вида.

#### SQL
> SQL (Structured Query Language, структурированный язык запросов) не является API или протоколом. Это декларативный язык: вы говорите, что вам нужно, вместо того, как это сделать. Это универсальный язык реляционных баз данных.

#### DDL
> DDL (Data Definition Language, язык определения данных) который обрабатывает создание, удаление,
ограничения и разрешения для таблиц, баз данных.

#### DML
> DML (Data Manipulation Language, язык манипулирования данными), который обрабатывает
добавление данных, их выборку, обновление и удаление.

Основные операции DML реляционной базы данных можно запомнить с помощью акронима `CRUD` - Create, Read, Update, Delete.

#### DB-API
[DB-API](https://legacy.python.org/dev/peps/pep-0249/) - это стандартный API в Python, предназначенный для получения доступа к реляционным базам данных. 

Примеры реляционный баз данных:

- [SQLite](http://www.sqlite.org/)
- [MySQL](http://www.mysql.com/)
  The most popular MySQL drivers for python:
  - [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
  - [PYMySQL](https://github.com/petehunt/PyMySQL/)
  - [oursql](http://pythonhosted.org/oursql/)
- [PostgreSQL](http://www.postgresql.org/)
  The most popular PostgreSQL drivers for python:
  - [psycopg2](http://initd.org/psycopg/)
  - [py-postgresql](https://github.com/python-postgres/fe)
- [SQLAlchemy](http://www.sqlalchemy.org/) - самая популярная библиотека для работы с разными базами данных.
- [dataset](https://dataset.readthedocs.org/) - database for lazy people.

### NoSQL database

> Они были созданы для работы с очень крупными наборами данных, позволяют более гибко определять данные и поддерживают пользовательские операции с данными.

NoSQL database example:

- Семейство `dbm` - они представляют собой хранилища, работающие по принципу «ключ — значение»
- [memcached](http://memcached.org/) - это быстрый сервер кэширования, располагающийся в памяти и работающий по принципу "ключ-значение"
- [redis](http://redis.io/) — это сервер структур данных. Как и в случае с memcached, все данные сервера Redis должны поместиться в память (хотя у нас имеется возможность сохранить все данные на диск).
  - [redis-py](https://github.com/andymccurdy/redis-py) driver
  - [redis-py](http://bit.ly/redis-py-docs) documentation
- Cassandra
- CouchDB
- HBase
- Kyoto
- MongoDB
- Riak
  
#### Redis How to
Windows:

- First of all in order to deploy `redis` on Windows we need enable `WSL` (Windows Subsystem for Linux), follow the instructions on [Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install-win10#install-the-windows-subsystem-for-linux)

- If `WSL` was deployed run these commands, from `bash`, to install `redis-server`

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install redis-server
redis-cli -v

sudo service redis-server restart
```

PS: Follow this guide to clarify more details: [Windows Subsystem for Linux (WSL)](https://redislabs.com/blog/redis-on-windows-10/)

### Fulltext databases

- Lucene
- Solr
- ElasticSearch
- Sphinx
- Xapian
- Whoosh

## WWW

### Web clients

- http
- urllib
- [requests](http://docs.python-requests.org/en/master/)

### Web frameworks

> Общий интерфейс шлюза (Common Gateway Interface, CGI) был разработан для того, чтобы веб-серверы могли запускать внешние программы и возвращать результаты.

> Web Server Gateway Interface (WSGI) — универсальный API между веб-приложениями и веб-серверами.

We can start simple http server in this way: python -m http.server

- [Bottle](https://bottlepy.org/docs/dev/) ("бутылка")
```
pip install bottle
```
- [Flask](http://flask.pocoo.org/) ("склянка")
```
pip install flask
```

Full-Stack [Web Frameworks](https://wiki.python.org/moin/WebFrameworks) for Python

### HTTP

"Передача состояния представления" (Representational State Transfer, `REST`)

> Многие продукты имеют REST-интерфейс или интерфейс RESTful. На практике это часто означает, что они имеют веб-интерфейс — определения URL, предназначенные для доступа к веб-сервису.

- `HEAD` - получает информацию о ресурсе, но не его данные;

- `GET` - GET получает данные ресурса с сервера. Это стандартный метод, используемый вашим браузером. В любое время, когда вы видите URL с вопросительным знаком (?), за которым следует несколько аргументов, вы можете распознать запрос GET. GET не должен использоваться для создания, изменения или удаления данных;

- `POST` - этот глагол обновляет данные на сервере. Он часто используется для HTML-форм и сетевых API;

- `PUT` - этот глагол создает новый ресурс;

- `DELETE` - этот глагол говорит сам за себя: DELETE удаляет.

[Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.

## System

### Datetime

Одним из способов представления абсолютного времени является подсчет количества секунд, прошедших с некоторой стартовой точки. В Unix используется количество секунд, прошедших с полуночи 1 января 1970 года (примерно в это время появилась система Unix). Это значение часто называют `epoch`

:point_up: Не забывайте: `UTC` для времени, `UTF-8` для строк

### Alternative datetime modules:

- [arrow](https://arrow.readthedocs.io/en/latest/) - содержит множество функций для работы с датой и временем и имеет простой API.
- [dateutil](https://dateutil.readthedocs.io/en/stable/) - может проанализировать любой формат даты и хорошо работает с относительными датами и временем.
- [iso8601](https://pypi.org/project/iso8601/) - заполняет пробелы, связанные с работой модулей стандартной библиотеки, когда речь идет о формате ISO 8601.
- [fleming](https://fleming.readthedocs.io/en/develop/) - содержит множество функций для работы с часовыми поясами.

## Concurrency

:point_up: В Python потоки не ускоряют задачи, связанные с ограничениями процессора, из-за одной детали реализации стандартной системы Python, которая называется Global Interpreter Lock (GIL). Она предназначена для того, чтобы избежать потоковых проблем в интерпретаторе Python, и действительно может замедлить многопоточную программу по сравнению с однопоточной или даже многопроцессорной версией.

### Synchronization:

:point_up: In general different python locks supports [context management protocol](https://docs.python.org/3/library/threading.html#with-locks).

### Networking frameworks

- [gevent](http://www.gevent.org/) - gevent is a coroutine -based Python networking library that uses greenlet to provide a high-level synchronous API on top of the libev or libuv event loop;
- [tornado](https://www.tornadoweb.org/en/stable/) - Tornado is a Python web framework and asynchronous networking library;
- [gunicorn](https://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX;
- [twisted](https://twistedmatrix.com) - Twisted is an event-driven networking engine written in Python;
- [asyncio](https://docs.python.org/3/library/asyncio.html) - asyncio is a library to write concurrent code using the async/await syntax.
- [pyzmq](http://zeromq.org/bindings:python) - Python binding for ZeroMQ library.
    - [pyzmq sources](https://github.com/zeromq/pyzmq) - github repo of pyzmq sources;
    - [pyzmq documentation](https://pyzmq.readthedocs.io/en/latest/) - PyZMQ Documentation.
    
Python socket [how to](https://docs.python.org/3/howto/sockets.html)

### Python queue packages:

- [Celery](http://www.celeryproject.org/) - Celery is an asynchronous task queue/job queue based on distributed message passing.
- [thoonk](https://pypi.org/project/thoonk/) - hoonk is a clusterable, Redis based, Publish-Subscribe, Queue, and Job Distrubtion system based on the philosophies of XMPP Pubsub
- [RQ (Redis Queue)](http://python-rq.org/) - simple Python library for queueing jobs and processing them in the background with workers.
- [Queues](https://python-scripts.com/queues) - этот сайт предлагает поучаствовать в дискуссии о программном обеспечении для создания очередей, как написанном на Python, так и ином.

### Message brokers

- [RabbitMQ](https://www.rabbitmq.com/) - the most widely deployed open source message broker;
- [PubSubHubbub](https://github.com/pubsubhubbub/) - an open, simple, web-scale and decentralized pubsub protocol;

### RPC

- [xmlrpc](https://docs.python.org/3/library/xmlrpc.html)
- [fabric](http://docs.fabfile.org/en/2.4/)
- [msgpack-rpc](https://github.com/msgpack-rpc/msgpack-rpc-python)

---

# Library references

## Random

[Random choices](https://docs.python.org/3/library/random.html#random.choices) with/without replacement [meaning](https://www.statisticshowto.datasciencecentral.com/sampling-with-replacement-without/)

## pydoc

```
**********************************************************************
    report.py
**********************************************************************

def add(x, y):
    """
    Add x and y
    >>> add(2, 3)
    5
    """
    return x + y
```

- Generate documentation with [pydoc](https://docs.python.org/3/library/pydoc.html) module: `pydoc -w .\report.py`. `report.html` file will be generated.
- Invoke test with [doctest](https://docs.python.org/3/library/doctest.html) module: `python -m doctest .\report.py -v`

---

# AWS IoT

## How to:

Application client usage:
```
python .\device-client.py -e a6406hrbnb143-ats.iot.us-east-2.amazonaws.com -r AmazonRootCA1.pem -c 96b5d1ce52-certificate.pem.crt -k 96b5d1ce52-private.pem.key -n testiot
```

Device client usage:
```
python .\app-client.py -e a6406hrbnb143-ats.iot.us-east-2.amazonaws.com -r AmazonRootCA1.pem -c 5a256deadb-certificate.pem.crt -k 5a256deadb-private.pem.key -n testiot
```

AWS IoT Python [SDK](https://github.com/aws/aws-iot-device-sdk-python)

AWS IoT Python [SDK Documentation](https://s3.amazonaws.com/aws-iot-device-sdk-python-docs/html/index.html)

AWS [IoT Core](https://docs.aws.amazon.com/iot/?id=docs_gateway) Documentation

---

# Tkinter

:point_up: Shows what version of Tcl/Tk is installed: `python -m tkinter`

## Ubuntu

:point_up: Provide tkinter support for python3: `sudo apt-get install python3-tk`

---

[Top](#table-of-contents)
