import urllib.request, urllib.parse, urllib.error
import json
import ssl

# 忽略SSL证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    # 使用你提供的示例URL作为默认值
    url = 'http://py4e-data.dr-chuck.net/comments_2225551.json' 

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    info = json.loads(data)
except:
    info = None

if not info:
    print('Failed to parse JSON')
    exit()

# 从info字典中获取comments列表
comments_list = info['comments']

print('Count:', len(comments_list))

total_sum = 0
for item in comments_list:
    total_sum += int(item['count'])

print('Sum:', total_sum)