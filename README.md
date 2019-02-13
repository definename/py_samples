# Install python with [anaconda](https://www.anaconda.com/)

## Update `anaconda` from older version:
```
conda update conda
conda update anaconda
```

## Uninstall `anaconda`:

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
