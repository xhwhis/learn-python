import socket

def client(i):
    s = socket.socket()
    s.connect(('127.0.0.1', 46574))
    print('Recv msg: %s, Client: %d' %(s.recv(1024), i))
    s.close()

if __name__ == '__main__':
    for i in range(10):
        client(i)
