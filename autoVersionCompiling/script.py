import PyInstaller.__main__
import os
from packaging.version import Version
import shutil

strInputPath = "test.py"
strBuildFilePath = "./build"
strAuthor = "Gian Rathgeb"

if strInputPath == "":
    print("No File Name set")
    exit

if not os.path.isfile(strBuildFilePath):
    buildInfo = open(strBuildFilePath, "w")
    buildInfo.write("0.0.0.0")
    buildInfo.close()

with open(strBuildFilePath, "r") as buildInfo:
    verLastVersion = Version(buildInfo.read())
with open(strBuildFilePath, "w") as buildInfo:
    arrNewVersion = [
        verLastVersion.release[0],
        verLastVersion.release[1],
        verLastVersion.release[2],
        verLastVersion.release[3],
    ]
    arrNewVersion[2] += 1
    strNewVersion = ""
    for index in arrNewVersion:
        strNewVersion += str(index) + "."
    # Everything but not last char (is . and don't work with version)
    strNewVersion = strNewVersion[0:-1]
    buildInfo.write(strNewVersion)
strCompileDirPath = str(f"{strInputPath[0:-3]}-{strNewVersion}")
try:
    os.mkdir(strCompileDirPath)
except OSError:
    print("Error while Compiling")
    exit
else:
    print(f"Created folder for compiled files: {strCompileDirPath}")
    shutil.copy(f"./{strInputPath}", f"{strCompileDirPath}")
    print(f"Copy {strInputPath} to {strCompileDirPath}")

    inputFile = str(f"{os.path.join(strCompileDirPath, strInputPath)}")
    outputFile = str(f"{strInputPath[0:-3]}-{strNewVersion}.py")
    outputPath = str(f"{os.path.join(strCompileDirPath, outputFile)}")
    os.rename(inputFile, outputPath)
    print(f"Renamed output file to {outputFile}")

    PyInstaller.__main__.run([
        '--distpath', strCompileDirPath, '--workpath', os.path.join(
            strCompileDirPath, "compile"), outputPath
    ])
    os.remove(f"{outputFile[0:-3]}.spec")
    shutil.rmtree(os.path.join(strCompileDirPath, "compile"))
