import socket

def server():
    s = socket.socket()
    host = '127.0.0.1'
    port = 46574
    s.bind((host, port))
    s.listen(5)

    while True:
        c, addr = s.accept()
        print('Connect Addr: ', addr)
        c.send(b'hello world')
        c.close()

if __name__ == '__main__':
    server()
