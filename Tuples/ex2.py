fname = input('Enter file name:')
time_str = str()
mail_dict = {}
try:
    fhand = open(fname)
except:
    print('ERROR!')
    exit()
mail_dict = {}
for line in fhand:
    if line.startswith('From '):
        list_line = line.split()
        if len(list_line) > 6:
            time_str = list_line[5]
            time_word = time_str.split(':')[0]
            mail_dict[time_word] = mail_dict.get(time_word,0) + 1

lst = list()
for key,value in mail_dict.items():
    lst.append((key,value))
lst.sort()
for key,value in lst:
    print(key,value)