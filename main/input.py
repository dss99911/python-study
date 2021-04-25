import sys

ok = input("input yes/no")
if ok in ('y', 'ye', 'yes'):
    print('y')
else:
    print('n')

# input from argv
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()