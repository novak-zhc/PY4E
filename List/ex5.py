fname = input('Enter a file name:')
fhand = open(fname)
mbox = []
count = 0
for line in fhand:
    if line.startswith('From '):
        mailwords = line.split()
        word = mailwords[1]
        mbox.append(word)
        count += 1
for address in mbox:
    print(address)
print(f"There were {count} lines in the file with From as the first word")