
import os
os.getcwd() #'C:\\Python39'
os.chdir('/server/accesslogs')
os.system('mkdir today')   # Run the command mkdir in the system shell

import sys
print(sys.argv)  # python3 system.py 1 2 => ['system.py', '1', '2']

print(dir(os))  # returns a list of all module functions
help(os) # show help page

# Shell util
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')

import glob
print(glob.glob('*.py')) # show files with .py


# args parser https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
import argparse
# python top.py --lines=5 alpha.txt beta.txt
parser = argparse.ArgumentParser(prog = 'top',
                                 description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args) # args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt']