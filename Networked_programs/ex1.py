import socket

try:
    # 1. 获取用户输入的URL
    url = input('Enter URL: ')
    
    # 2. 解析URL，提取主机名和路径
    # 例如：'http://data.pr4e.org/romeo.txt'
    # .split('/') 会得到 ['http:', '', 'data.pr4e.org', 'romeo.txt']
    host = url.split('/')[2]
    # 构建HTTP GET请求的路径部分
    path = url.split(host, 1)[1]
    
    # 3. 创建和连接套接字
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    
    # 4. 构建并发送HTTP GET请求
    cmd = ('GET ' + path + ' HTTP/1.0\r\nHost: ' + host + '\r\n\r\n').encode()
    mysock.send(cmd)

    # 5. 接收并打印数据
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')

    # 6. 关闭连接
    mysock.close()

except IndexError:
    print('Invalid URL format. Please use a full URL like http://example.com/file.txt')
except Exception as e:
    print(f'An error occurred: {e}')