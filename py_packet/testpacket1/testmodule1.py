from . import testmodule2

def test_module1_func():
    return f"This function '{testmodule2.test_module2_func()}' is called from '{test_module1_func.__name__}'"