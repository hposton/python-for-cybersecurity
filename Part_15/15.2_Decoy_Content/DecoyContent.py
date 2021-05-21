import pathlib

def getTimestamps(filename):
    fname = pathlib.Path(filename)
    stats = fname.stat()
    if not fname.exists(): # File deleted
        return []
    return(stats.st_ctime,stats.st_mtime,stats.st_atime)
    

def checkTimestamps(filename,create,modify,access):
    stats = getTimestamps(filename)
    if len(stats) == 0:
        return False # File deleted
    (ctime,mtime,atime) = stats
    if float(create) != float(ctime):
        return False    # File creation time is incorrect
    elif float(modify) != float(mtime):
        return False    # File modify time is incorrect
    elif float(access) != float(atime):
        return False    # File access time is incorrect
    return True

def checkDecoyFiles():
    with open("decoys.txt","r") as f:
        for line in f:
            vals = line.rstrip().split(",")
            if not checkTimestamps(vals[0],vals[1],vals[2],vals[3]):
                print("%s has been tampered with." % vals[0])

checkDecoyFiles()
