
import sys
from libs.printf import *


def main(argv):
	if len(argv) != 2:
		printf_line("usage: {} [FILE]", argv[0])
		return 0
	with open(argv[1], 'rt') as infile:
		print(infile.read().count('\n'))

main(sys.argv)
