import socket

client = socket.socket()
client.connect(('10.200.60.152', 9999))
name = input("Enter name : ")
client.send(bytes(name, 'utf-8'))
msg = client.recv(1024).decode()
print(msg)
while True:
    msg_s = input("#")
    if msg_s == "exit":
        client.send(bytes(msg_s, 'utf-8'))
        break
    client.send(bytes(msg_s, 'utf-8'))
    msg_r = client.recv(1024).decode()
    print(msg_r)