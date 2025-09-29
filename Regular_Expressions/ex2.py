import re

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    exit()

numbers_list = []
for line in fhand:
    line = line.strip()
    # 使用 findall() 提取所有匹配的数字
    numbers = re.findall(r'[0-9]+', line)
    # findall() 返回一个列表。如果找到了匹配，列表不为空
    if len(numbers) > 0:
        # 将提取到的字符串数字转换为整数并添加到列表中
        for number_str in numbers:
        # 将每个字符串数字转换为整数并添加到列表中
            numbers_list.append(int(number_str))

fhand.close()

# 计算平均值
'''
if len(numbers_list) > 0:
    average = sum(numbers_list) / len(numbers_list)
    print(int(average))
else:
    print("No matching lines found.")
'''
#打印总值
if len(numbers_list) > 0:
    test_sum = sum(numbers_list)
    print(int(test_sum))