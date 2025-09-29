f_number = 0
count = 0
fname = input('Enter the file name:')
fhand = open(fname)
for line in fhand:
    line =line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    line = str(line)
    cut_line = line
    line = cut_line[19:]
    line = float(line)
    f_number = f_number + line
avg_number = f_number / count
print('Average spam confidence:',avg_number)