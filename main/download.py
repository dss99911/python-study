import subprocess

import tempfile

import urllib

import os
from io import BytesIO
from zipfile import ZipFile

filename = os.path.join("dir", 'model')


def download_unzip_file():
    url = urllib.request.urlopen("http://download.geonames.org/export/zip/IN.zip")
    with ZipFile(BytesIO(url.read())) as my_zip_file:
        for contained_file in my_zip_file.namelist():
            if contained_file == "IN.txt":
                with my_zip_file.open(contained_file, 'r') as data:
                    print(data)  # TODO how to save?


def un_tar():
    with tempfile.TemporaryDirectory() as tmpdirname:
        output_filename = os.path.join(tmpdirname, 'model')

        tc = subprocess.call([
            "tar",
            "xzf",
            output_filename,
            f"--directory={tmpdirname}",
        ])
        assert tc == 0, 'tar error'
        print('extracted', str(os.listdir(tmpdirname)))
