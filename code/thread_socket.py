#encode=utf-8
from socket import *
from multiprocessing import *
from time import sleep


# 客户端的请求并为其服务

def dealWithClient ():
	while True:
		recv_data = new_socket.recv(1024)
		if len(recv_data) > 0:
			print('recv[%s]:%s'%(str(destAddr), recvData))
		else:
			print('[%s]客户端已经关闭'%str(destAddr))
			break
		new_socket.close()


def main ():
	ser_socket = socket(AF_INET, SOCK_STREAM)
	ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	local_addr = ('', 7788)
	ser_socket.bind(local_addr)
	ser_socket.listen(5)

	try:
		while True:
			print('等待客户端')
			new_socket, dest_addr = ser_socket.accpet()
		
			print('父进程[%s]'%str(dest_addr))
			client = Thread(target=deal_width_client, args=(new_socket, dest_addr))
			client.start()
	finally:
		ser_socket.close()

if __name__ == '__main__':
	main()
