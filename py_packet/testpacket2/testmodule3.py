from testpacket1.testmodule1 import test_module1_func as tmf1

def test_module3_func():
    return f"Function call in module3:{tmf1()}"