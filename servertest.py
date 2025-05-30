import socket

sock = socket.socket()

sock.bind(('127.0.0.1', 8001))
sock.listen(5)
while True:
    conn, addr = sock.accept() # 阻塞等待客户端连接
    data = conn.recv(1024)
    print(f"客户端发送的请求信息:{data}")
    
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8;servername=myserver\r\n\r\nhello world')
    conn.close()