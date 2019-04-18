import importlib
import time
import testreload

while True:
    time.sleep(1)
    importlib.reload(testreload)
