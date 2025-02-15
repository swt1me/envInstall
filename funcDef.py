import os

def runCommand(command):

    os.system(command)
def checkPackageManager():
    return "apt"

def installPackage(software):
    runCommand(f"sudo {checkPackageManager()} install {software}")

def cloneRepo(repo):
    runCommand(f"git clone {repo}")

def buildRepo(sourceCodeDir):
    runCommand(f"cd {sourceCodeDir} && mkdir build&& cmake ..&& make&& make install")
