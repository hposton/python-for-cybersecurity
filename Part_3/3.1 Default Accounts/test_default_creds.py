import paramiko
import telnetlib
    
def SSHLogin(host,port,username,password):
    try: 
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host,port=port,username=username,password=password);
        ssh_session = ssh.get_transport().open_session()
        if ssh_session.active:
            print("Login successful on %s:%s with username %s and password %s" % (host,port,username,password))
    except:
            print("Login failed %s %s" % (username,password))
    ssh.close()
    
def TelnetLogin(host,port,username,password):
    h = "http://"+host+":"+port+"/"
    tn = telnetlib.Telnet(h)
    tn.read_until("login: ")
    tn.write(username + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")
    try: 
        result = tn.expect(["Last login"])
        if (result[0] > 0):
            print("Telnet login successful on %s:%s with username %s and password %s" % (host,port,username,password))
        tn.close()
    except EOFError:
        print("Login failed %s %s" % (username,password))

host = "127.0.0.1"
port = 2200
with open("defaults.txt","r") as f:
    for line in f:
        vals = line.split()
        username = vals[0].strip()
        password = vals[1].strip()
        SSHLogin(host,port,username,password)
        TelnetLogin(host,port,username,password)
        
