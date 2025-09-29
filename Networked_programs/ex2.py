import socket

try:
    url = input('Enter URL: ')
    
    # 1. 修正 URL 解析逻辑
    host = url.split('/')[2]
    path = url.split(host, 1)[1]
    
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    
    cmd = ('GET ' + path + ' HTTP/1.0\r\nHost: ' + host + '\r\n\r\n').encode()
    mysock.send(cmd)

    count = 0

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        
        # 将接收到的数据解码为字符串
        decoded_data = data.decode()
        
        # 检查是否应该继续打印
        if count < 3000:
            # 计算还可以打印多少字符
            remaining = 3000 - count
            # 打印最多 remaining 个字符
            print(decoded_data[:remaining], end='')
            
        # 累计总字符数
        count = count + len(decoded_data)

    mysock.close()

    # 打印最终的字符总数
    print(f"\nTotal characters: {count}")
    
except IndexError:
    print('Invalid URL format. Please use a full URL like http://example.com/file.txt')
except Exception as e:
    print(f'An error occurred: {e}')