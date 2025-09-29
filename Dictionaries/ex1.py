fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('Error!')
word_dict = {}
for line in fhand:
    words = line.split()
    for word in words:
        word_dict[word] = True
test = input("Enter a word to check: ")
if test in word_dict:
    print(f"{test} is in the dictionary")
else:
    print(f"{test} is NOT in the dictionary")




