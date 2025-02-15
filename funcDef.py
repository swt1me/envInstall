import os

def runCommand(command):

    os.system(command)
def checkPackageManager():
    return "apt"

def installPackage(software):
    runCommand(f"sudo {checkPackageManager()} install {software}")

def cloneRepo(ssl,repo):
    runCommand(f"git clone -c http.sslVerify={ssl} {repo}")

def buildRepo(sourceCodeDir):
    runCommand(f"cd {sourceCodeDir} &&mkdir build &&cd build && cmake .. &&make && make install")
