from scapy.all import *
from base64 import b64decode
import re

def ExtractFTP(packet):
    payload = packet[Raw].load.decode("utf-8").rstrip()
    if payload[:4] == 'USER':
        print("%s FTP Username: %s" % (packet[IP].dst,payload[5:]))
    elif payload[:4] == 'PASS':
        print("%s FTP Password: %s" % (packet[IP].dst,payload[5:]))

emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
unmatched = []
def ExtractSMTP(packet):
    payload = packet[Raw].load
    try:
        decoded = b64decode(payload)
        decoded = decoded.decode("utf-8")
        connData = [packet[IP].src,packet[TCP].sport]
        if re.search(emailregex,decoded):
            print("%s SMTP Username: %s" % (packet[IP].dst,decoded))
            unmatched.append([packet[IP].src,packet[TCP].sport])
        elif connData in unmatched:
                print("%s SMTP Password: %s" % (packet[IP].dst,decoded))
                unmatched.remove(connData)
            
    except:
        return

awaitingLogin = []
awaitingPassword = []
def ExtractTelnet(packet):
    
    try:
        payload = packet[Raw].load.decode("utf-8").rstrip()
    except:
        return
    connData = [packet[IP].src,packet[TCP].sport] # Assume server is source
    if payload[:5] == "login":
        awaitingLogin.append(connData)
        return
    elif payload[:8] == "Password":
        awaitingPassword.append(connData)
        return
    connData = [packet[IP].dst,packet[TCP].dport] # Assume client is source
    if connData in awaitingLogin:
        print("%s Telnet Username: %s" % (packet[IP].dst,payload))
        awaitingLogin.remove(connData)
    elif connData in awaitingPassword:
        print("%s Telnet Password: %s" % (packet[IP].dst,payload))
        awaitingPassword.remove(connData)

packets = rdpcap("merged.pcap")

for packet in packets:
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        if packet[TCP].dport == 21:
            ExtractFTP(packet)
        elif packet[TCP].dport == 25:
            ExtractSMTP(packet)
        elif packet[TCP].sport == 23 or packet[TCP].dport == 23:
            ExtractTelnet(packet)