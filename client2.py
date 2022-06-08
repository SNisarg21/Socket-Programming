import socket

s = socket.socket()
print(socket.gethostbyname(socket.gethostname()))

# import socket
#
# client = socket.socket()
# client.connect(('localhost', 9999))
# name = input("Enter name : ")
# client.send(bytes(name, 'utf-8'))
# msg = client.recv(1024).decode()
# print(msg)
# while True:
#     msg_s = input("#")
#     if msg_s == "exit":
#         client.send(bytes(msg_s, 'utf-8'))
#         break
#     client.send(bytes(msg_s, 'utf-8'))
#     msg_r = client.recv(1024).decode()
#    print(msg_r)