#  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
f = open('workfile', 'w')
f.readline()  # read 1 line
for line in f:  # read each line in for
    print(line, end='')

# with : after open, it's closed automatically
with open('workfile') as f2:
    read_data = f2.read()  # if size parameter is omitted, all content is read.
