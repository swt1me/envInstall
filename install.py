import funcDef
import define

software_num = 0
repo_num = 0

is_ssl = input("是否启用git ssl(是/否)：")
is_ssl_if = "false"
loop_num = 0

while software_num != 2:
    funcDef.installPackage(define.softwareList[software_num])
    software_num += 1

while repo_num != 2:
    if is_ssl_if != "true":
        is_ssl_if = "true"
        if is_ssl == "是":
            ssl = "true"
        elif is_ssl == "否":
            ssl = "false"
    funcDef.cloneRepo(ssl,define.hostingPlatform + define.repoLists[repo_num])
    repo_num += 1

while loop_num != 2:
    funcDef.buildRepo(define.sourceCodeDir[loop_num])
    repo_num += 1