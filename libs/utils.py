
import sys

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

EXIT_NORMAL = 0
EXIT_ERROR = 1
EXIT_ARGUMENT_ERROR = 2

def run_main(func):
    sys.exit(func(sys.argv) or 0)
