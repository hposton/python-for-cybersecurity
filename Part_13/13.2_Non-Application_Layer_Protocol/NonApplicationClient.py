from scapy.all import *

def transmit(message, host):
    for m in message:
        packet = IP(dst=host)/ICMP(code = ord(m))
        send(packet)

host = "3.20.135.129"
message = "Hello"
transmit(message,host)