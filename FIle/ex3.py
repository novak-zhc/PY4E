import sys
count = 0
fname = input('Enter the file name:')
try:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')
        sys.exit()
    fhand = open(fname)
    for line in fhand:
        line = line.strip()
        if line.startswith('From '):
            count = count + 1           
except:
    print('File cannot be opened:',fname)
print(f"There were {count} subject lines in {fname}")