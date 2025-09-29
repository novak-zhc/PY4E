fname = input('Enter file name:')
max_count = None
max_mail = None
try:
    fhand = open(fname)
except:
    print('File NAME ERROR!')
    exit()

mail_dict = {}
for line in fhand:
    if line.startswith('From '):
        list_line = line.split()
        if len(list_line) > 2:
            word = list_line[1]
            mail_dict[word] = mail_dict.get(word,0) + 1

for mail,count in mail_dict.items():
    if max_count is None or count > max_count:
        max_count = count
        max_mail = mail

print(max_mail,max_count)

#sort the dictionary
lst = list()
for key,val in mail_dict.items():
    lst.append((val,key))
lst.sort(reverse=True)

print(lst[0])



















