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

# Functions:

`Функции` - это именованый фрагмент кода, отделенный от других

`Замыкание` — это функция, которая динамически генерируется другой функцией, и они обе могут изменяться и запоминать значения переменных, которые были созданы вне функции.
