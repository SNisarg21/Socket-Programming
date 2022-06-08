import socket
from threading import *

s = socket.socket()
s.bind(("10.200.60.152", 9999))
s.listen(3)

while True:
    class oneConn(Thread):
        def run(self) -> None:
            conn, addr = s.accept()
            name = conn.recv(1024).decode()
            print(name, addr)
            conn.send(bytes(f"Welcome {name}", 'utf-8'))
            while True:
                msg = conn.recv(1024).decode()
                if msg == "exit":
                    print(f">>{name}>>Left the Conversation")
                    conn.close()
                else:
                    print(f">>{name}>> ", msg)
                msg_s = input(">>Admin>>")
                conn.send(bytes(msg_s, 'utf-8'))
                if msg == "exit":
                    print(f">>{name}>>Left the Conversation")

    class two(Thread):
        def run(self) -> None:
            conn, addr = s.accept()
            name = conn.recv(1024).decode()
            print(name, addr)
            conn.send(bytes(f"Welcome {name}", 'utf-8'))
            while True:
                msg = conn.recv(1024).decode()
                if msg == "exit":
                    print(f">>{name}>>Left the Conversation")
                    conn.close()
                else:
                    print(f">>{name}>> ", msg)
                msg_s = input(">>Admin>>")
                conn.send(bytes(msg_s, 'utf-8'))
                if msg == "exit":
                    print(f">>{name}>>Left the Conversation")

    conn1 = oneConn()
    conn2 = two()

    conn1.start()
    conn2.start()



