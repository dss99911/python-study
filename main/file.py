#  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
import os
import shutil
from os import listdir, path
from os.path import isfile, join
from os import walk
import zipfile


def copy_file(src, dst):
    from shutil import copyfile
    copyfile(src, dst)

def read_file():
    f = open('workfile', 'r')
    f.readline()  # read 1 line
    for line in f:  # read each line in for
        print(line, end='')

def read_str_from_file(path):
    with open(path, "r") as f:
        return f.read()


def write_file():
    with open("Output.txt", "w") as text_file:
        text_file.write("code")


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


def get_current_dir():
    os.path.dirname(__file__)


def get_dir(file_path):
    os.path.dirname(file_path)



def is_dir():
    os.path.isdir("path")

def remove_folder():
    """
    delete not empty folder
    :return:
    """
    shutil.rmtree('folder_name', ignore_errors=True)

def remove_file():
    os.remove("some_path")

#%%
import os
import zipfile


def zipdir(dir_path, zip_path, exclude: list = None):
    zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)

    # ziph is zipfile handle

    def is_exclude(p):
        if exclude is None:
            return False
        for e in exclude:
            if p.startswith(e):
                print(f"exclude {apath}")
                return True
        return False

    for root, dirs, files in os.walk(dir_path):
        if is_exclude(root):
            continue

        for file in files:
            apath = os.path.join(root, file)
            if is_exclude(apath):
                continue

            zipf.write(apath, os.path.relpath(apath, os.path.join(dir_path, '..')))

    zipf.close()

zipdir(".", "python.zip", exclude=["./python.zip"])

def unzip(zip_path, dir_path):
    import zipfile
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dir_path)

#%%
# "a/b" 를 안하고, join을 쓰는 이유는 windows와 mac등 다른 플랫폼에서도 가능하게 하기 위한 것 일듯.
os.path.join("a", "b")

#%%

if __name__ == '__main__':
    mkdir("a")
