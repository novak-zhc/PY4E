fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('ERROR!')
    exit()

domain_dict = {}
for line in fhand:
    if line.startswith("From "):
        list_line = line.split()
        if len(list_line) > 2:
            p_line = list_line[1]
            domain_word = p_line.split('@')[1]
            domain_dict[domain_word] = domain_dict.get(domain_word,0) + 1

