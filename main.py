# server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = 12345

s.bind(('127.0.0.1', port))


s.listen(5)

while True:
    c, addr = s.accept()
    c.send(str('Thank you for connecting').encode('utf8'))
    play_mode = c.recv(1024).decode('utf8')
    print(play_mode)
    c.close()
