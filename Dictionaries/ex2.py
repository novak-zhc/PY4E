fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('Error!')
    exit()
week_dict = {}
for line in fhand:
    if line.startswith('From '):
        week_line = line.split()
        if len(week_line) > 2:
            words = week_line[2]
            week_dict[words] = week_dict.get(words,0) + 1

print(week_dict)