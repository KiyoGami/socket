#server.py 

import socket 

host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(2)
print("Server listening on port", port)

while True:
    c, addr = s.accept()
    print("Connect from ", str(addr))
    msg = c.recv(1024).decode()
    while msg:
        c.send(f"{msg.upper()}".encode())
        if msg == 'break': break
        msg = c.recv(1024).decode()
    #server sử dụng kết nối gửi dữ liệu tới client dưới dạng binary
    c.close()
    if msg == 'break': break

s.close()