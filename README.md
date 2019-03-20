# Table of contents

- [Containers](#containers)
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

> Pip is a package manager + Virtualenv is an environment manager = [Conda](https://conda.io/en/latest/) is both

# [Anaconda](https://www.anaconda.com/) environment:

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

## [Uninstall](https://docs.anaconda.com/anaconda/install/uninstall/) `anaconda`:

:one:
Install clean up tool:
```
conda install anaconda-clean
```

:two:
Remove all Anaconda-related files and directories without being prompted to delete each one
```
anaconda-clean --yes
```

:three:
On `Windows` remove `anaconda` with `Control Panel`. On `Linux` with command `rm -rf ~/anaconda`

---

# [Visual Studio Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) configuration

## Configure interpreter

:one: Install `python` extention

:two: Select `python` interpreter
- ctrl+shift+p
- type `python: select interpreter`
- select `python` interpreter from the list of available interpreters

As result `.vscode` folder will be created with `settings.json` file.  Inside of `setting.json` file `python.pythonPath` variable will point to the `python` interpreter.

## Configure and run debugger

- Set breakpoint
- ctrl+shift+d (go to debugging tab)
- Select `python: current file`
- Run debugging by pressing `F5`

---

# [jupyter nbviewer](https://nbviewer.jupyter.org/)

Create `*.ipynb` file and share it via `nbviewer` service

---

# containers

List(Список) - `[1, 2, 3, "one", "two", "three"]`
- Изменяемый контейнер

Tuple(Кортеж) - `(1, 2, 3, 4, 5)`
- Неизменяемый контейнер(только на первом уровне), если в `tuple` добавить `list` его мдно будет изменить

Dictionary(Словарь) - `{ "seconds": "1", "minutes": "2", "hour": "3", "day": "4", "month": "5", "year": "5" }`
- Получение структуры данных в виде `ключ`: `значение`

Set(Множество) - `{1, 2, 3, 4, 5, 6, 0}`
- Решение задачи получения уникальных элементов

---

# concepts

:boom: `Включение` — это компактный способ создать структуру данных из одного или более итераторов.

```
list - [ выражение for элемент in итерабельный объект ]
dict - { выражение_ключа: выражение_значения for выражение in итерабельный объект }
set - { выражение for выражение in итерабельный объект }
```

:boom: `Функции` - это именованый фрагмент кода, отделенный от других.

:boom: `Замыкание` — это функция, которая динамически генерируется другой функцией, и они обе могут изменяться и запоминать значения переменных, которые были созданы вне функции.

:boom: В Python `лямбда-функция` — это анонимная функция, выраженная одним выражением.

:boom: В Python `генератор` — это объект, который предназначен для создания последовательностей.

:boom: `Декоратор` — это функция, которая принимает одну функцию в качестве аргумента и возвращает другую функцию.

:boom: `Пространства имен` — разделы, внутри которых определенное имя уникально и не связано с такими же именами в других пространствах имен.

:boom: В Python используются `исключения`: код, который выполняется, когда происходит связанная с ним ошибка.

---

# module

:boom: `Модуль` — это всего лишь файл, содержащий код Python

> Eсли вы знакомы с книгой Gamma E. Design Patterns: Elements of Reusable Object-Oriented Software, можете использовать модули в Python как синглтоны

To create python module it is enough to create file `modulename.py`

In order to import python `module` we need to do the following: `import modulename`
It is also possible to import module and create alias for it in this way: `import modulename as mn`

To be able to import only specific function from python module we need to do the following: `from modulename import functionname`
To do the same with alias: `from modulename import functionname as fn`

## Generate documentation and tests

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

- Generate documentation with `pydoc` module: `pydoc -w .\report.py`. `report.html` file will be generated.
- Invoke test with `doctest` module: `python -m doctest .\report.py -v`

---

# package

:boom: Модули организованные в иерархии файлов называются `пакетами`

In order to create `python` package we need to create directory and put all `*.py` files into that folder. Also `__init__.py` file should be created inside that folder to tell python is it should interpret that folder as package.

---

# class

:boom: `наследование` — создание нового класса из уже существующего, который при этом содержит какие-то дополнения и изменения

В Python *геттеры* и *сеттеры* не нужны, поскольку все атрибуты и методы являются открытыми, а от вас ожидается примерное поведение!

In order to make class attributes private we need to decorate their names with `__` e.g `__name`

:boom: `полиморфизм` — это значит, что одна операция может быть произведена над разными объектами независимо от их класса.

---

# namespace

It works according to the given rule - `LEGB`

---

# data

:point_up:

`cтроки` — последовательности символов в кодировке Unicode, используемые для представления текстовых данных.

`байты и массивы байтов` — последовательности восьмибитных целых чисел, используемые для представления двоичных данных.

`unicode` — это действующий международный стандарт, определяющий символы всех языков мира плюс математические и другие символы.

`UTF-8` — динамическую схему кодирования, oна использует для символа Unicode от одного до четырех байтов.

---

# format

Python предлагает два способа форматирования строк, их часто называют `старым` стилем и `новым` стилем.

:point_up:

Старый стиль форматирования строк имеет форму `строка % данные`

Новый стиль форматирования имеет формат `'{} {} {}'.format(a, b, c)`

---

# regex

`.` - любой символ

`*` - любое количество предыдущих елементов

`.*` - любое количество символов (даже ноль)

`?` - ноль или одно включение (опциональный символ)

`\b` - граница слова: `<граница слова>fish<граница слова>` -> `\bfish\b`

---

# serialization

Сохранение структур данных в файл называется `сериализацией`

Library to serialize data as binary:

- [msgpack](https://msgpack.org/)
- [protobuf](https://github.com/protocolbuffers/protobuf)
- [avro](http://avro.apache.org/docs/current/)
- [thrift](http://thrift.apache.org/)

Поскольку они бинарные, ни один из них не может быть изменен человеком, вооружившимся текстовым редактором.

[HDF5](http://www.hdfgroup.org/why_hdf) — это бинарный формат данных, предназначенный для хранения многомерных или иерархических числовых данных.

---

# Databases

## Relational Database

> Relational Databases (pеляционная база данных) представляет собой множество взаимосвязанных таблиц, каждая из которых содержит информацию об объектах определенного вида.

### SQL
> SQL (Structured Query Language, структурированный язык запросов) не является API или протоколом. Это декларативный язык: вы говорите, что вам нужно, вместо того, как это сделать. Это универсальный язык реляционных баз данных.

### DDL
> DDL (Data Definition Language, язык определения данных) который обрабатывает создание, удаление,
ограничения и разрешения для таблиц, баз данных.

### DML
> DML (Data Manipulation Language, язык манипулирования данными), который обрабатывает
добавление данных, их выборку, обновление и удаление.

Основные операции DML реляционной базы данных можно запомнить с помощью акронима `CRUD` - Create, Read, Update, Delete.

### DB-API
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

---

## NoSQL database

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

---

## Fulltext databases

- Lucene
- Solr
- ElasticSearch
- Sphinx
- Xapian
- Whoosh

---

# WWW

## Web clients

- http
- urllib
- [requests](http://docs.python-requests.org/en/master/)

## Web frameworks

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

## HTTP

"Передача состояния представления" (Representational State Transfer, `REST`)

> Многие продукты имеют REST-интерфейс или интерфейс RESTful. На практике это часто означает, что они имеют веб-интерфейс — определения URL, предназначенные для доступа к веб-сервису.

- `HEAD` - получает информацию о ресурсе, но не его данные;

- `GET` - GET получает данные ресурса с сервера. Это стандартный метод, используемый вашим браузером. В любое время, когда вы видите URL с вопросительным знаком (?), за которым следует несколько аргументов, вы можете распознать запрос GET. GET не должен использоваться для создания, изменения или удаления данных;

- `POST` - этот глагол обновляет данные на сервере. Он часто используется для HTML-форм и сетевых API;

- `PUT` - этот глагол создает новый ресурс;

- `DELETE` - этот глагол говорит сам за себя: DELETE удаляет.

[Scrapy](https://scrapy.org/) - An open source and collaborative framework for extracting the data you need from websites.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - Beautiful Soup is a Python library for pulling data out of HTML and XML files.

---

# System

## Datetime

Одним из способов представления абсолютного времени является подсчет количества секунд, прошедших с некоторой стартовой точки. В Unix используется количество секунд, прошедших с полуночи 1 января 1970 года (примерно в это время появилась система Unix). Это значение часто называют `epoch`

:point_up: Не забывайте: `UTC` для времени, `UTF-8` для строк

## Alternative datetime modules:

- [arrow](https://arrow.readthedocs.io/en/latest/) - содержит множество функций для работы с датой и временем и имеет простой API.
- [dateutil](https://dateutil.readthedocs.io/en/stable/) - может проанализировать любой формат даты и хорошо работает с относительными датами и временем.
- [iso8601](https://pypi.org/project/iso8601/) - заполняет пробелы, связанные с работой модулей стандартной библиотеки, когда речь идет о формате ISO 8601.
- [fleming](https://fleming.readthedocs.io/en/develop/) - содержит множество функций для работы с часовыми поясами.

[Top](#table-of-contents)
