import socket
import threading
import requests
from cryptography.fernet import Fernet


def start():
    global NeedNewThread
    NeedNewThread = True
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 7000))
    s.listen(10)
    key = b'1y25dI9dfpIkuXAtSroOw16bWhjt8jiDAaCpe2wXr1Y='  #
    cipher_suite = Fernet(key)
    while (1):
        print("waiting for request ...");
        conn, address = s.accept()
        data = conn.recv(10000)
        worker(data, cipher_suite)
        # t = threading.Thread(target=worker, args=(data, cipher_suite))
        # t.start()


def worker(data, cipher_suite):
    print("a thread is starting...")
    plain_text = cipher_suite.decrypt(data)
    print(data)
    print(plain_text)
    temp = "http://"
    temp = temp + plain_text.decode("utf-8")
    answer = "403 FORBIDDEN REQUEST"
    print('send request to server')
    if "POST" in temp:
        answer = requests.post(temp)
    elif "GET" in temp:
        answer = requests.get("http://www.aut.ac.ir")
    # else :
    #     print("this message is ignored ")
    #     # have to do something
    print(answer)


start()
