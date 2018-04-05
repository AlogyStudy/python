#coding=utf-8
import socket
import re
import sys

from multiprocessing import Process


# 设置静态文件根目录
HTML_ROOT_DIR = './html'

WSGI_PYTHON_DIR = './wsg_python'

class HttpServer(object):
    def __init__(self):
        self.ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, port):
        self.ser_sock.bind(('', port))

    def start(self):
        self.ser_sock.listen(128)

        while True:
            cli_sock, cli_address = self.ser_sock.accept()
            print('[%s, %s]用户链接了'%cli_address)
            hand_process = Process(target=self.hand_client, args=(cli_sock, ))
            hand_process.start()
            cli_sock.close()

    def hand_client(self, cli_sock):
        request_data = cli_sock.recv(1024)
        print('--- requset_data %s ---'%request_data)
        request_lines = request_data.splitlines()

        for line in request_lines:
            print(line)
        
        # 解析请求报文
        # GET / HTTP/1.1
        request_start_line = request_lines[0]
        file_name = re.match(r'\w+\s+(/[^ ]*)', request_start_line.decode('utf-8')).group(1)
        method = re.match(r'(\w+)\s+/[^ ]*', request_start_line.decode('utf-8')).group(1)

        if file_name.endswith('.py'):
            try:
                module = __import__(file_name[1:-3])
            except Exception:
                self.response_headers = 'HTTP/1.1 404 Not Found\r\n'
                response_body = 'not found'
            else:
                env = {
                    "PATH_INFO": file_name,
                    "METHOD": method
                }
                # 容错处理
                response_body = module.application(env, self.start_response)
            response = self.response_headers + '\r\n' + response_body
        else:    
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
    def start_response(self, status, headers):
        server_headers = [
            ('Server', 'My server')
        ]
        response_headers = 'HTTP/1.1 ' + status + '\r\n'
        for header in headers:
            response_headers += '%s: %s\r\n'%header
        self.response_headers = response_headers

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HttpServer()
    http_server.bind(7329)
    http_server.start()

if __name__ == '__main__':
    main()
 