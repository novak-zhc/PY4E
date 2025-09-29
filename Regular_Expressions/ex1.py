import re
regex_input = input('Enter a regular expression: ')
fname = 'mbox.txt' 


try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
 
    if re.search(regex_input, line):
        count = count + 1

print(f'{fname} had {count} lines that matched {regex_input}')

fhand.close()