import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")  # extra value
parser.add_argument("-f", "--fast", dest="fast", action="store_true")  # existence/nonexistence
args = parser.parse_args()
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