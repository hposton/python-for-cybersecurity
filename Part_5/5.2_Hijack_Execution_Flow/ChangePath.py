import os, winreg

def readPathValue(reghive,regpath):
    reg = winreg.ConnectRegistry(None,reghive)
    key = winreg.OpenKey(reg,regpath,access=winreg.KEY_READ)
    index = 0
    while True:
        val = winreg.EnumValue(key,index)
        if val[0] == "Path":
            return val[1]
        index += 1

def editPathValue(reghive,regpath,targetdir):
    path = readPathValue(reghive,regpath)
    newpath = targetdir + ";" + path
    reg = winreg.ConnectRegistry(None,reghive)
    key = winreg.OpenKey(reg,regpath,access=winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key,"Path",0,winreg.REG_EXPAND_SZ,newpath)
    
# Modify user path
#reghive = winreg.HKEY_CURRENT_USER
#regpath = "Environment"
targetdir = os.getcwd()

#editPathValue(reghive,regpath,targetdir)

# Modify SYSTEM path
reghive = winreg.HKEY_LOCAL_MACHINE
regpath = "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
editPathValue(reghive,regpath,targetdir)
