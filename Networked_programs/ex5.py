import urllib.request
from bs4 import BeautifulSoup
import ssl

# 忽略 SSL 证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. 获取用户输入的 URL
url = input('Enter URL: ')

# 2. 从 URL 读取 HTML 内容并进行解析
print('Retrieving:', url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# 3. 找到所有的 span 标签
tags = soup('span')
count = 0
total_sum = 0

# 4. 遍历标签，提取数字并求和
for tag in tags:
    # 提取标签内的文本内容
    number_string = tag.contents[0]
    
    # 将文本内容转换为整数
    try:
        number = int(number_string)
        total_sum += number
        count += 1
    except ValueError:
        # 如果转换失败，则跳过该标签
        continue

# 5. 打印最终结果
print('Count:', count)
print('Sum:', total_sum)