> Pip is a package manager + Virtualenv is an environment manager = [Conda](https://conda.io/en/latest/) is both

# [anaconda](https://www.anaconda.com/) environment:

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

# [jupyter nbviewer](https://nbviewer.jupyter.org/)

Create `*.ipynb` file and share it via `nbviewer` service

# Containers:

List(Список) - `[1, 2, 3, "one", "two", "three"]`

Tuple(Кортеж) - `(1, 2, 3, 4, 5)`

Dictionary(Словарь) - `{ "seconds": "1", "minutes": "2", "hour": "3", "day": "4", "month": "5", "year": "5" }`

Set(Множество) - `{1, 2, 3, 4, 5, 6, 0}`

# Сoncepts:

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


# Module:

:boom: `Модуль` — это всего лишь файл, содержащий код Python

To create python module it is enough to create file `modulename.py`

In order to import python `module` we need to do the following: `import modulename`
It is also possible to import module and create alias for it in this way: `import modulename as mn`

To be able to import only specific function from python module we need to do the following: `from modulename import functionname`
To do the same with alias: `from modulename import functionname as fn`

# Package:

Модули организованные в иерархии файлов называются `пакетами`

In order to create `python` package we need to create directory and put all `*.py` files into that folder. Also `__init__.py` file should be created inside that folder to tell python is it should interpret that folder as package.
