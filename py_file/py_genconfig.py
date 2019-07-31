import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

def main():
    finename = "config.cfg"
    log.debug(f"Config file: {finename} is being generated...")
    with open(file="config.cfg", mode="wt") as ofile:
        ofile.write("[rmcp]\n")
        ofile.write("resend = 5\n")
        ofile.write("request_timeout = 5\n")
        ofile.write("identify_timeout = 1\n")
        ofile.write("is_heartbeat = True\n")
        ofile.write("heatbeat_timeout = 1\n")

        ofile.write("\n[uart]\n")
        ofile.write("port = ~/serial2\n")
    log.debug("Done...")


if __name__ == "__main__":
    main()
