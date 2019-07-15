import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    num = int("7fff", 16)
    num += 1
    # In order not to generate number more that 7fff(32767)
    num = num & 0x7fff
    log.debug(num)

if __name__ == "__main__":
    main()
