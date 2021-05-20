import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--decimal", dest="decimal", action="store")  # extra value
parser.add_argument("-f", "--fast", dest="fast", action="store_true")  # existence/nonexistence
args = parser.parse_args()


# 1
# True

if __name__ == '__main__':
    print(args.decimal)
    print(args.fast)