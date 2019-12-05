
import sys
import io

#   some IO functions

def get_file_size(file):
    file.seek(0, io.SEEK_END)
    size = file.tell()
    file.seek(0, io.SEEK_SET)

def read_file(file):
    size = get_file_size(file)
    buffer = bytearray(size)

    read_number = file.readinto(buffer)
    if read_number != size:
        raise EOFError(format('while reading: {}', file.name))

    return buffer

def read_file_name(name):
    with open(name, 'rb', 0) as file:
        return read_file(file)

def get_signed_string(signed):
    return 'signed' if signed else 'unsigned'

def read_int(infile, *, size = 1, byteorder = 'big', signed = False):
    _buffer = infile.read(size)
    if len(_buffer) != size:
        raise EOFError('reading {} byte {} int'.format(size, get_signed_string(signed)))
    return int.from_bytes(_buffer, byteorder, signed = signed)
