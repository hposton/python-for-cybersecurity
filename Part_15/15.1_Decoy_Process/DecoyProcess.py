import signal,sys
from time import sleep

def terminated(signum,frame):
    pass


signal.signal(signal.SIGTERM,terminated)
signal.signal(signal.SIGINT,terminated)
while True:
    siginfo = signal.sigwaitinfo({signal.SIGINT,signal.SIGTERM})
    with open("terminated.txt","w") as f:
        f.write("Process terminated by %d\n" % siginfo.si_pid)
    sys.exit(0)
