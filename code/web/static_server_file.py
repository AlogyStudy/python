#coding=utf-8
import socket
import re

from multiprocessing import Process


# 设置静态文件根目录
HTML_ROOT_DIR = './html'

def hand_client(cli_sock):
    request_data = cli_sock.recv(1024)
    print('--- requset_data %s ---'%request_data)
    request_lines = request_data.splitlines()

    for line in request_lines:
        print(line)
    
    # 解析请求报文
    # GET / HTTP/1.1
    request_start_line = request_lines[0]
    file_name = re.match(r'\w+\s+(/[^ ]*)', request_start_line.decode('utf-8')).group(1)
    if '/' == file_name: # 常量写在右边，变量写在左边
        file_name = '/index.html'

    # 打开文件，读取内容
    try:
        file = open(HTML_ROOT_DIR + file_name, 'rb')
    except IOError:
        response_data_line = 'HTTP1.1 404 not found\r\n'
        response_data_head = 'Server: alogy server\r\n'
        response_data_body = 'the file is not found!'
    else:            
        file_data = file.read()
        file.close()    
        # 构造客户端返回数据
        response_data_line = 'HTTP1.1 200 OK\r\n'
        response_data_head = 'Server: alogy server\r\n'
        response_data_body = file_data.decode('utf-8')

    response = response_data_line + response_data_head + '\r\n' + response_data_body
    print('response data:', response)
    cli_sock.send(bytes(response, 'utf-8'))
    cli_sock.close()

def main():
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ser_sock.bind(('', 7329))
    ser_sock.listen(127)

    while True:
        cli_sock, cli_address = ser_sock.accept()
        print('[%s, %s]用户链接了'%cli_address)
        hand_process = Process(target=hand_client, args=(cli_sock, ))
        hand_process.start()
        cli_sock.close()

if __name__ == '__main__':
    main()
 