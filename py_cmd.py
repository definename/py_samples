import cmd
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {name} {levelname} - {message}", style="{")
log = logging.getLogger()

class MyShell(cmd.Cmd):
    intro = 'Welcome to the my! shell.   Type help or ? to list commands.\n'
    prompt = '$'

    def do_do(self, arg):
        'do:  do 100'
        arg_list = parse(arg)
        if len(arg_list) == 0:
            log.error("Invalid params were given")
        else:
            log.debug("Done! with params: {}".format(parse(arg)))

    def do_exit(self, arg):
        'exit: stop doing and exit...'
        log.debug("Thank you for using my! shell")
        return True

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    try:
        MyShell().cmdloop()
    except KeyboardInterrupt:
        log.error("Key")
        pass
    except Exception as e:
        log.error("Error occurred: {}".format(e))