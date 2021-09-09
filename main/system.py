
import os
os.getcwd() #'C:\\Python39'
os.chdir('/server/accesslogs')
os.system('mkdir today')   # Run the command mkdir in the system shell
os.system('pip install slack_sdk')   # install package

import sys
print(sys.argv)  # python3 system.py 1 2 => ['system.py', '1', '2']

print(dir(os))  # returns a list of all module functions
help(os) # show help page
#%%

#%%
# Shell util
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

import glob
print(glob.glob('*.py')) # show files with .py

