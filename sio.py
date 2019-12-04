
import sys
import io

#   some IO functions

def read_file_name(name):
    with open(name, 'rb', 0) as file:
        return read_file(file)

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
