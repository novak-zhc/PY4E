import string
fname = input('Enter file name:')
letters_dict = {}
try:
    fhand = open(fname)
except:
    print('File NAME ERROR!')
    exit()
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    for char in line:
        if 'a' <= char <='z':
            letters_dict[char] = letters_dict.get(char,0) + 1

sorted_list = []
for letter, count in letters_dict.items():
    sorted_list.append((count, letter))

# 对列表进行降序排序（最高计数在前）
sorted_list.sort(reverse=True)

# 打印排序后的结果
for count, letter in sorted_list:
    print(letter, count)
