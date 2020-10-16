# Import modules
import PyInstaller.__main__
import os
from packaging.version import Version
import shutil
# Output with color
from colorama import Fore, init
# After print reset color
init(autoreset=True)

# Import writeVersionfile.py
import writeVersionFile as vf

# Define variables (i.e. input path)
strInputPath = "test.py"
strProjectName = "Test Script"
strBuildFilePath = "./build"
strAuthor = "Gian Rathgeb"
strVersionFile = "versionFile.txt"

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
elif strProjectName == "":
    print("Project name not given")
    exit
elif strVersionFile == "":
    print("Version file not given")
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
arrNewVersion = [
    verLastVersion.release[0],
    verLastVersion.release[1],
    verLastVersion.release[2],
    verLastVersion.release[3],
]
# Update the patch level in new version
arrNewVersion[2] += 1
# Build string with new version
strNewVersion = ""
for index in arrNewVersion:
    strNewVersion += str(index) + "."
# Everything but not last char (is . and don't work with version)
strNewVersion = strNewVersion[0:-1]


# Create the output path for the compiled file
strCompileDirPath = str(f"{strInputPath[0:-3]}-{strNewVersion}")
# Try to create this directory
try:
    os.mkdir(strCompileDirPath)
except OSError:
    print(f"{Fore.RED}Error while Compiling")
    exit
else:
    # Copy script to compiled folder
    print(f"{Fore.BLUE}Created folder for compiled files: {strCompileDirPath}")
    shutil.copy(f"./{strInputPath}", f"{strCompileDirPath}")
    print(f"{Fore.BLUE}Copy {strInputPath} to {strCompileDirPath}")

    # Rename the copied script (oldname-version)
    strInputFile = str(f"{os.path.join(strCompileDirPath, strInputPath)}")
    strOutputFile = str(f"{strInputPath[0:-3]}-{strNewVersion}.py")
    strOutputPath = str(f"{os.path.join(strCompileDirPath, strOutputFile)}")
    os.rename(strInputFile, strOutputPath)
    print(f"{Fore.BLUE}Renamed output file to {strOutputFile}")

    # Write version file
    vf.writeVersionFile(strVersionFile, tuple(arrNewVersion),
                        strAuthor, strProjectName, strNewVersion)

    print(f"{Fore.BLUE}Begin compiling {strInputPath}")
    # Run Pyinstaller and compile script
    PyInstaller.__main__.run([
        '--version-file=../%s' % strVersionFile,
        '--onefile',
        '--specpath',
        strCompileDirPath,
        '--distpath',
        strCompileDirPath,
        '--workpath',
        os.path.join(strCompileDirPath, "compile"),
        strOutputPath,
    ])
    # Remove unnecessary files and dirs (temporary generated files)
    strSpecFile = f"{strOutputFile[0:-3]}.spec"
    os.remove(f"{os.path.join(strCompileDirPath, strSpecFile)}")
    shutil.rmtree(os.path.join(strCompileDirPath, "compile"))

    print(f"{Fore.BLUE}Compiled script {strInputPath} to {strOutputPath}")

    # Open buildfile with write rights and write new version to file
    with open(strBuildFilePath, "w") as buildInfo:
        # Write new version to build file
        buildInfo.write(strNewVersion)

    print(f"{Fore.BLUE}Write new version ({strNewVersion}) to file")