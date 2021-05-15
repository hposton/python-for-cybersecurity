from scapy.all import *

flowData = {}
def analyzeFlow(p):
    if p.haslayer(IP):
        length = p[IP].len
    else:
        return
    key = None
    data = None
    if p[IP].src < p[IP].dst:
        key = ','.join([p[IP].src,p[IP].dst])
        data = [length,0]
    else:
        key = ','.join([p[IP].dst,p[IP].src])
        data = [0,length]
    if key in flowData:
        f = flowData[key]
        flowData[key] = [f[0]+data[0],f[1]+data[1]]
    else:
        flowData[key] = data

packets = rdpcap("http.cap")
for p in packets:
    analyzeFlow(p)

for f in flowData:
    [src,dst] = f.split(",")
    d = flowData[f]
    print("%d bytes %s->%s\t%d bytes %s->%s" % (d[0],src,dst,d[1],dst,src))