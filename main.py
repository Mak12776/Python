
import sys

char_range = lambda start, stop, step = 1: map(chr, range(ord(start), ord(stop), step))
print(list(char_range('a', 'z')))

