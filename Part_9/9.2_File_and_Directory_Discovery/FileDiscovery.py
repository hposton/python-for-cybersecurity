import os,re
from zipfile import ZipFile

email_regex = '[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'
phone_regex = '[(]*[0-9]{3}[)]*-[0-9]{3}-[0-9]{4}'
ssn_regex = '[0-9]{3}-[0-9]{2}-[0-9]{4}'
regexes = [email_regex, phone_regex, ssn_regex]
def findPII(data):
    matches = []
    for regex in regexes:
        m = re.findall(regex,data)
        matches += m
    return matches

def printMatches(filedir,matches):
    if len(matches) > 0:
        print(filedir)
        for match in matches:
            print(match)
    

def parseDocx(root,docs):
    for doc in docs:
        matches = None
        filedir = os.path.join(root,doc)
        with ZipFile(filedir,"r") as zip:
            data = zip.read("word/document.xml")
            matches = findPII(data.decode("utf-8"))
        printMatches(filedir,matches)

def parseText(root,txts):
    for txt in txts:
        filedir = os.path.join(root,txt)
        with open(filedir,"r") as f:
            data = f.read()
        matches = findPII(data)
        printMatches(filedir,matches)

txt_ext = [".txt",".py",".csv"]

def findFiles(directory):
    for root,dirs,files in os.walk(directory):
        parseDocx(root,[f for f in files if f.endswith(".docx") ])
        for ext in txt_ext:
            parseText(root,[f for f in files if f.endswith(ext)])

directory = os.path.join(os.getcwd(),"Documents")
findFiles(directory)