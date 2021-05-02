#  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
import os
from os import listdir, path
from os.path import isfile, join
from os import walk


def read_file():
    f = open('workfile', 'r')
    f.readline()  # read 1 line
    for line in f:  # read each line in for
        print(line, end='')


def read_file_with(file_path):
    # with : after open, it's closed automatically
    with open(file_path) as f2:
        read_data = f2.read()  # if size parameter is omitted, all content is read.
        print(read_data)


def list_files_name(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def list_files_name2(path):
    _, _, filenames = next(walk(path))
    return filenames


def list_files_path(path: str):
    return list(map(lambda x: f"{path.rstrip('/')}/{x}", list_files_name(path)))


def mkdir(file_path: str):
    if not path.exists(file_path):
        os.mkdir(file_path)


if __name__ == '__main__':
    print(list_files_path("./modules/"))