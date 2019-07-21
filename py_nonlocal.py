import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

x = 99

def main():
    x = 100
    def foo():
        log.debug(f"x: {x}")
    foo()

if __name__ == "__main__":
    main()