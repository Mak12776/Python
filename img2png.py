
import sys
from libs.sio import read_int
from PIL import Image

class FileStructureError(Exception):
    pass

IMG_MAGIC = b'img.'

def img2png(infile, outfile):
    magic = infile.read(len(IMG_MAGIC))
    if magic != IMG_MAGIC:
        raise FileStructureError(
            'invalid file magic number: {!r}'.format(magic))

    size_width = read_int(infile, 1, signed = False)

    color_width = read_int(infile, size_width, signed = False)

    if color_width == 1:
        mode = "L"
    elif color_width == 2:
        mode = "LA"
    elif color_width == 3:
        mode = "RGB"
    elif color_width == 4:
        mode = "RGBA"
    else:
        raise FileStructureError('unknown color width: {}'.format(color_width))

    width = read_int(infile, size_width, signed = False)
    height = read_int(infile, size_width, signed = False)

    data = infile.read()
    if len(data) != width * height * color_width:
        raise FileStructureError('invalid size of data: {}'.format(len(data)))

    print('image size: {}, {}'.format(width, height))
    print('image mode: {}'.format(mode))

    img = Image.frombytes(mode, (width, height), data)
    img.save(outfile, 'png')

def replace_ext(name, repl):
    index = name.rfind('.')
    if index == -1:
        return name + '.' + repl
    else:
        return name[:index] + '.' + repl

def main(argv):
    if len(argv) == 2:
        infile_name = argv[1]
        outfile_name = replace_ext(infile_name, 'png')
    elif len(argv) == 3:
        infile_name, outfile_name = argv[1:]
    else:
        print('usage: python {} <INFILE> [OUTFILLE]'.format(argv[0]))
        return 0
    with open(infile_name, 'rb') as infile:
        with open(outfile_name, 'wb') as outfile:
            img2png(infile, outfile)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
