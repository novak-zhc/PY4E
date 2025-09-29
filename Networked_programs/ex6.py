import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# 忽略 SSL 证书错误
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 获取用户输入并转换为整数
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# 核心逻辑：循环跟随链接
while count > 0:
    print('Retrieving:', url)
    
    try:
        # 访问 URL 并解析
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # 找到所有 'a' 标签
        tags = soup('a')
        
        # 检查链接是否存在以避免索引错误
        if len(tags) >= position:
            # 找到指定位置的链接，并更新 url
            url = tags[position - 1].get('href', None)
            
            # 如果url不存在（例如为None），则退出循环
            if url is None:
                print("Link not found at the specified position.")
                break
        else:
            print("Not enough links on the page.")
            break
            
    except urllib.error.URLError as e:
        print(f"Error retrieving URL: {e.reason}")
        break
    
    # 循环计数器减1
    count -= 1

# 提取最后一个名字并打印
try:
    final_name = url.split('_')[2].split('.')[0]
    print("The answer is:", final_name)
except Exception as e:
    print("Could not extract the final name from the URL.")
    print("Final URL:", url)
# Code: https://www.py4e.com/code3/urllinks.py