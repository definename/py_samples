import logging
import argparse

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="file", help="Source file path", required=True)
    parser.add_argument("-s", dest="search", help="Search statement", required=True)
    args = parser.parse_args()

    log.debug("Search:'{}' in '{}'".format(args.search, args.file))

    found_list = []
    with open(file=args.file, mode="rt") as stream:
        line_n = 0
        for line in stream:
            line_n += 1
            if args.search in line:
                found_list.append((line_n, line.rstrip("\n")))

    if len(found_list) == 0:
        log.debug("Nothing found...")
    else:
        for line_n, line in found_list:
            log.debug("N:{} L:{}".format(line_n, line))

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log.exception("{}".format(e))