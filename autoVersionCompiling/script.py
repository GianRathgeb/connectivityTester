import PyInstaller
import os
from packaging.version import parse, Version

strInputPath = "main.py"
strBuildFilePath = "autoVersionCompiling/build"

if strInputPath == "":
    print("No File Name set")
    exit

if not os.path.isfile(strBuildFilePath):
    buildInfo = open(strBuildFilePath, "w")
    buildInfo.write("0.0.0.0")
    buildInfo.close()
else:
    with open(strBuildFilePath, "r") as buildInfo:
        verLastVersion = Version(buildInfo.read())
    with open(strBuildFilePath, "w") as buildInfo:
        arrNewVersion = [verLastVersion.release[0], verLastVersion.release[1], verLastVersion.release[2], verLastVersion.release[3]]
        arrNewVersion[2] += 1
        strNewVersion = ""
        for index in arrNewVersion:
            strNewVersion += str(index) + "."
        # Everything but not last char (is . and don't work with version)
        buildInfo.write(strNewVersion[0:-1])
