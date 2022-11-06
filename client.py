#client .py

import socket 

s = socket.socket()
s.connect(("localhost", 4000)) 

while True:
    data = input()

    s.send(data.encode())
    msg = s.recv(1024)

    print('Uppercase: ', msg.decode())
    if data == 'break': break

s.close()
