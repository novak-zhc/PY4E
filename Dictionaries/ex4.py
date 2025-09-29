fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('ERROR!')
    exit()
mail_dict = {}

for mail_line in fhand:
    if mail_line.startswith('From '):
        mails = mail_line.split()
        if len(mails) > 2:
            mail = mails[1]
            mail_dict[mail] = mail_dict.get(mail,0) + 1
#print(mail_dict)

bigemail = None
bigcount = None


for email, count in mail_dict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email


print(bigemail, bigcount)