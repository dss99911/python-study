pip install "package-name"
#install package with version
pip install "package-name==version"

#upgrading pip
python -m pip install -U pip

#upgrade pip
pip install -U "package-name"

#show version
pip show "package-name"

#Error case : Cannot uninstall 'PyYAML'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
#https://stackoverflow.com/a/53534728/4352506
pip install --ignore-installed PyYAML