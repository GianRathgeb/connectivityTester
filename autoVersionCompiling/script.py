# Import modules
import PyInstaller.__main__
import os
from packaging.version import Version
import shutil

# Define variables (i.e. input path)
strInputPath = "test.py"
strBuildFilePath = "./build"
strAuthor = "Gian Rathgeb"

# Check if variables are defined
if strInputPath == "":
    print("No file name set")
    exit
elif strBuildFilePath == "":
    print("No path to the build file set")
    exit
elif strAuthor == "":
    print("The author is not given")
    exit

# Check if the build file exists, if not generate it
if not os.path.isfile(strBuildFilePath):
    # Generate file
    buildInfo = open(strBuildFilePath, "w")
    # Write first version to it (0.0.0.0)
    buildInfo.write("0.0.0.0")
    buildInfo.close()

# Read the last compiled version from the file
with open(strBuildFilePath, "r") as buildInfo:
    verLastVersion = Version(buildInfo.read())
# Define the new version and set it equal to last verison
with open(strBuildFilePath, "w") as buildInfo:
    arrNewVersion = [
        verLastVersion.release[0],
        verLastVersion.release[1],
        verLastVersion.release[2],
        verLastVersion.release[3],
    ]
    # Update the patch version in new version
    arrNewVersion[2] += 1
    # Build string with new version
    strNewVersion = ""
    for index in arrNewVersion:
        strNewVersion += str(index) + "."
    # Everything but not last char (is . and don't work with version)
    strNewVersion = strNewVersion[0:-1]
    # Write new version to build file
    buildInfo.write(strNewVersion)
# Create the output path for the compiled file
strCompileDirPath = str(f"{strInputPath[0:-3]}-{strNewVersion}")
# Try to create this directory
try:
    os.mkdir(strCompileDirPath)
except OSError:
    print("Error while Compiling")
    exit
else:
    # Copy script to compiled folder
    print(f"Created folder for compiled files: {strCompileDirPath}")
    shutil.copy(f"./{strInputPath}", f"{strCompileDirPath}")
    print(f"Copy {strInputPath} to {strCompileDirPath}")

    # Rename the copied script (oldname-version)
    inputFile = str(f"{os.path.join(strCompileDirPath, strInputPath)}")
    outputFile = str(f"{strInputPath[0:-3]}-{strNewVersion}.py")
    outputPath = str(f"{os.path.join(strCompileDirPath, outputFile)}")
    os.rename(inputFile, outputPath)
    print(f"Renamed output file to {outputFile}")

    # Run Pyinstaller and compile script
    PyInstaller.__main__.run([
        '--onefile',
        '--specpath',
        strCompileDirPath,
        '--distpath',
        strCompileDirPath,
        '--workpath',
        os.path.join(strCompileDirPath, "compile"),
        outputPath,
    ])
    # Remove unnecessary files and dirs (temporary generated files)
    strSpecFile = f"{outputFile[0:-3]}.spec"
    os.remove(f"{os.path.join(strCompileDirPath, strSpecFile)}")
    shutil.rmtree(os.path.join(strCompileDirPath, "compile"))
