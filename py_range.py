import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    payload = random.choices(population=list(range(256)), k=int('ffff', 16))
    log.debug(f"len: {len(payload)}, chunk:{payload[-10:]}")

if __name__ == "__main__":
    main()