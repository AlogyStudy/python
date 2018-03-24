
#eoding=utf-8
import select
import sys
import socket


running = True

def main ():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 7788))
    server.listen(5)

    inputs = [server]

    while True:
      readable, writeable, exceptionsal = select.select(inputs, [], [])

      for sock in readable:
        if sock == server:
          client, addr = server.accept()
          inputs.append(client)
        
        # 监听用户输入的键盘
        elif sock == sys.stdin:
          cmd = sys.stdin.readline()
          running = False
          break

        else:
          data = sock.recv(1024)
          if data:
            sock.send(data)
          else:
            inputs.remove(data)
            sock.close()

      if not running:      
        break

    server.close()    

if __name__ == '__main__':
	main()