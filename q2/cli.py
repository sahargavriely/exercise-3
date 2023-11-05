import inspect
import sys


class CommandLineInterface:
    cmds_to_args = dict()
    cmds_to_function = dict()

    def command(self, f):
        self.cmds_to_args[f.__name__] = inspect.getfullargspec(f).args
        self.cmds_to_function[f.__name__] = f

    def main(self):
        file, *argv = sys.argv
        try:
            cmd, *args = argv
            args = {k: v for k, v in [arg.split('=') for arg in args]}
            injection_order = [args[k] for k in self.cmds_to_args[cmd]]
        except:
            print(f'USAGE: python {file} <command> [<key>=<value>]*')
            sys.exit(1)
        try:
            self.cmds_to_function[cmd](*injection_order)
        except Exception as error:
            print(f'ERROR: {error}')
            sys.exit(1)
