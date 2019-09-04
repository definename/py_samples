from .testmodule2 import test_module2_func as tmf2

def test_module1_func():
    return f"Function call in module1:{tmf2()}"