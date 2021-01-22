import socket
from Crypto.Cipher import AES

host = "127.0.0.1"
port = 1337

key = b"Sixteen byte key"

def decrypt(data,key,iv):
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(data)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn,addr = s.accept()
    with conn:
        while True:
            iv = conn.recv(16)
            length = conn.recv(1)   # Assumes short messages
            data = conn.recv(1024)
            if not data:
                break
            print("Received: %s"%decrypt(data,key,iv).decode("utf-8")[:ord(length)])