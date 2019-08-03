import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

x = 1
y = 1
def foo():
    global z
    z = x + y
    return z

def foo1():
    import py_global as my
    glob = globals()
    glob["x"] += 1

def local_and_global_access():
    import __main__ as main
    log.debug(f"Global x: {main.x}")
    x = 99
    log.debug(f"Local x: {x}")

def main():
    # Create global var in function.
    log.debug(f"create global z: {foo()}")
    log.debug(f"global z: {z}")

    # Change global var with build-in function.
    log.debug(f"x: {x}")
    foo1()
    log.debug(f"x: {x}")

    # Access global and local variable with the same name
    local_and_global_access()


if __name__ == "__main__":
    main()