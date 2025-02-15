import funcDef
import define

software_num = 0
repo_num = 0

while software_num != 2:
    funcDef.installPackage(define.softwareList[software_num])
    software_num += 1

while repo_num != 1:
    funcDef.cloneRepo(define.hostingPlatform + define.repoLists[repo_num])
    repo_num += 1

while repo_num != 1:
    funcDef.buildRepo(define.repoLists[repo_num])
    repo_num += 1