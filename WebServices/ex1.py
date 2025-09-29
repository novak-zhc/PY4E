import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# 忽略SSL证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 1. 获取URL
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2225550.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

# 2. 获取并解码XML数据
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

# 3. 使用XPath查找所有<count>标签
counts_list = tree.findall('.//count')

# 4. 统计数量并求和
count_sum = 0
for item in counts_list:
    count_sum += int(item.text)

print('Count:', len(counts_list))
print('Sum:', count_sum)