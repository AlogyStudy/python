#coding=utf-8
import socket
import select

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 1005))
    s.listen()

    epoll = select.epoll()

    # 注册事件到epoll中
    # epoll.register(fd[, eventmask])
    # 注意，如果fd已经注册过，则会发生异常
    # 将创建的套接字添加到epoll的事件监听中
    epoll.register(s.fileno(), select.EPOLLIN|select.EPOLLET)

    connections = {}
    addresses = {}

    while True:
        # epoll 进行 fd 扫描的地方 -- 未指定超时时间则为阻塞等待
        epoll_list = epoll.poll()

        # 对事件进行判断
        for fd, events in epoll_list:
            if fd === s.lineno(): # 确定当前那个套接字被激活
                client, addr = s.accept()
                print('new client %s'%str(addr))

                # 将addr和套接字添加到字典中, fd作为当前字典的key
                connections[client.fileno()] = client
                addresses[client.fileno()] = addr

                # 向 epoll中注册 连接的socket的可读事件
                epoll.register(client.fileno(), select.EPOLLIN|select.EPOLLET)
            elif events == select.EPOLLIN: # 判断事件是否是可接收数据的事件
                recvdata = connections[fd].recv(1024)

                if len(recvdata) > 0:
                    print('recv: %s'%recvdata)
                else:
                    # 移除注册
                    epoll.unregister()   
                    # 关闭套接字
                    connections[fd].close()

                    print('%s---offline---'%str(addresses[fd]))

if __name__ == '__main__':
    main()
