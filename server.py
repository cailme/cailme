import socket

ip_port = ('0.0.0.0', 60)
back_log = 5
buffer_size = 1024
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
ser.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
ser.bind(ip_port)  
ser.listen(back_log)  
while True:
    con, address = ser.accept() 
    while True:
        msg = con.recv(buffer_size).decode('utf-8')
        if msg == 'over':
            break
        print('server receive:', msg)
    print('server close')
    con.close()
