import socket

p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.connect(('192.168.101.16', 60))
while 1:
    msg = input('client send:')
    if not msg:
        continue
    p.send(msg.encode('utf-8'))  
    if msg == 'over':
        break
p.close()
