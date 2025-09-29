fname = input('Enter the file name:')
fhand = open(fname)
for line in fhand:
    line = line.upper()
    print(line.strip())
