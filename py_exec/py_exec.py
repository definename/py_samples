import logging
logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger(__name__)

def main():
    exec(open("testexec.py").read())
    exec("log.info('It works!!')")

if __name__ == "__main__":
    main()