from scapy.all import *

def printData(x):
    d = chr(x[ICMP].code)
    print(d,end="",flush=True)

sniff(filter="icmp", prn=printData)
