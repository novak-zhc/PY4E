import urllib.request

try:
    url = input('Enter URL: ')
    fhand = urllib.request.urlopen(url)

    # 一次性读取整个文档内容
    document = fhand.read()

    # 将字节串解码为字符串
    decoded_document = document.decode()

    # 打印前3000个字符
    print(decoded_document[:3000])

    # 计算并打印总字符数
    count = len(decoded_document)
    print(f"\nTotal characters: {count}")

except urllib.error.URLError as e:
    print(f"Error opening URL: {e.reason}")
except IndexError:
    print('Invalid URL format.')
except Exception as e:
    print(f'An error occurred: {e}')
