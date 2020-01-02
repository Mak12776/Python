
import sys
import os
import re
from libs.printf import printf_line

DEFAULT_FORMAT = '{count[0]:12}{count[1]:12}{count[2]:12}  {name:12}'

def count_file(path):
    line_num = 1
    char_num = 0
    word_num = 0
    with open(path) as f:
        for line in f:
            word_num += len(re.findall('\w+', line, re.ASCII))
            char_num += len(line)
            line_num += 1
    return line_num, word_num, char_num

def file_iter(path, pattern=None):
    if pattern is None:
        if os.path.isfile(path):
            yield path
        elif os.path.isdir(path):
            for name in os.listdir(path):
                fpath = os.path.join(path, name)
                if os.path.isfile(fpath):
                    yield fpath
                else:
                    yield from file_iter(fpath)
        else:
            raise FileNotFoundError('"{}" not exists.'.format(path))
    else:
        if os.path.isfile(path):
            name = os.path.basename(path)
            if re.fullmatch(pattern, name):
                return path
            yield path
        elif os.path.isdir(path):
            for name in os.listdir(path):
                fpath = os.path.join(path, name)
                if os.path.isfile(fpath):
                    if re.fullmatch(pattern, name):
                        yield fpath
                else:
                    yield from file_iter(fpath, pattern)
        else:
            raise FileNotFoundError('"{}" not exists.'.format(path))


def count(path, rformat=DEFAULT_FORMAT, pattern=None, result='return'):
    if result not in ('return', 'print'):
        raise ValueError('invalid result argument: {}'.format(result))
    res = []
    total = [0, 0, 0]
    for npath in file_iter(path, pattern):
        try:
            count = count_file(npath)
            for i in range(3):
                total[i] += count[i]
            res.append((os.path.basename(npath), count))
        except UnicodeDecodeError:
            continue
    if result == 'return':
        return total, res
    elif result == 'print':
        for n, c in res:
            print(rformat.format(name=n, count=c))
        print('\n' + rformat.format(name='total', count=total))
    else:
        raise ValueError('invalid result: ' + result)

def main(argv):
    if len(argv) != 2:
        printf_line('usage: {} [PATH]', argv[0])
        return 0
    count(argv[1], result = 'print')

if __name__ == '__main__':
    sys.exit(main(sys.argv))