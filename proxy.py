import socket
import threading
from cryptography.fernet import Fernet


def start():
    socket_receive = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_receive.bind(('127.0.0.1', 5000))

    socket_receive.listen(10)
    key = b'1y25dI9dfpIkuXAtSroOw16bWhjt8jiDAaCpe2wXr1Y='  # Fernet.generate_key()
    print(key)
    cipher_suite = Fernet(key)

    print("[*] initializing proxy ")
    while (1):
        try:
            # print "connect"
            conn, addr = socket_receive.accept()
            data = conn.recv(10000)
            t = threading.Thread(target=worker, args=(data, cipher_suite))
            t.start()


        except:
            socket_receive.close()


def worker(data, cipher_suite):
    print("a thread is starting...")
    cipher_text = cipher_suite.encrypt(data)
    print(data)
    print(cipher_text)
    sock_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_send.connect(('127.0.0.1', 7000))
    sock_send.send(cipher_text)
    print("[*] send cipher text to server")
    # t = requests.post("127.0.0.1:7000", data={'cipher': cipher_text });


start()
