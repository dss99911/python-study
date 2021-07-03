#  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
import os
import shutil
from os import listdir, path
from os.path import isfile, join
from os import walk


def read_file():
    f = open('workfile', 'r')
    f.readline()  # read 1 line
    for line in f:  # read each line in for
        print(line, end='')


def read_file_all(file_path):
    # with : after open, it's closed automatically
    with open(file_path) as f2:
        return f2.read()  # if size parameter is omitted, all content is read.


def list_files_name(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def list_files_name2(path):
    _, _, filenames = next(walk(path))
    return filenames


def list_files_path(path: str):
    return list(map(lambda x: f"{path.rstrip('/')}/{x}", list_files_name(path)))


def mkdir(file_path: str):
    if not path.exists(file_path):
        # os.mkdir(file_path)
        os.makedirs(file_path)

def get_dir():
    os.path.dirname(__file__)


def remove_folder():
    """
    delete not empty folder
    :return:
    """
    shutil.rmtree('folder_name', ignore_errors=True)

if __name__ == '__main__':
    mkdir("a")
