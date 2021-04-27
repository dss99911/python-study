import sys



if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv)) # first argument is python file name
    print('Arg0:', str(sys.argv[0]))
    print('Arg1:', str(sys.argv[1]))