import argparse
# args parser https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")  # extra value
parser.add_argument("-f", "--fast", dest="fast", action="store_true")  # existence/nonexistence
parser.add_argument('--foobar', action='store_true')
args = parser.parse_args() # if there is not added arguments, then occurs error
args, _ = parser.parse_known_args()  # ignore not added arguments

getattr(args, "port")
args.port

# python top.py --lines=5 alpha.txt beta.txt
parser = argparse.ArgumentParser(prog = 'top',
                                 description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args) # args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt']

#%%
# https://github.com/google/python-fire
# make CLI parameter automatically.
import fire

def hello(name="hyun"):
    print(f"Hello {name}")

if __name__ == '__main__':
    fire.Fire(hello)

#%%


# 1
# True

if __name__ == '__main__':
    print(args.decimal)
    print(args.fast)