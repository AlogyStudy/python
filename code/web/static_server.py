#coding=utf-8
import socket
from multiprocessing import Process


def handle_client(cli_socket):
    """ 处理客户端请求 """
    # 获取客户端请求数据
    request_data = cli_socket.recv(1024)
    print('resquest', request_data)

    # 构造响应数据
    response_start_line = 'HTTP/1.1 200 OK\r\n'
    response_start_head = 'Server: My Server\r\n'
    response_start_body = 'hello world'
    response = response_start_line + response_start_head + '\r\n' + response_start_body
    print('response: data:', response)

    # 向客户端返回数据
    cli_socket.send(bytes(response, 'utf-8'))
    cli_socket.close()

def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('', 7777))
    server_sock.listen(128)
    while True:
        cli_sock, cli_address = server_sock.accept()
        print('[%s, %s]用户连接上了'%cli_address)
        handle_client_process = Process(target=handle_client, args=(cli_sock, ))
        handle_client_process.start()
        cli_sock.close()

if __name__ == '__main__':
    main()
