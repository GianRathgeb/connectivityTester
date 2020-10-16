import os
from colorama import init, Fore
init(autoreset=True)


def writeVersionFile(strVersionFile, tupleVersion, strAuthor, strName, strVersion):
    print(f"{Fore.BLUE}Write Verison file")
    try:
        with open(strVersionFile, 'w') as vf:
            vf.write(f"""VSVersionInfo(
                ffi=FixedFileInfo(
                    filevers={tupleVersion},
                    prodvers={tupleVersion},
                    mask=0x3f,
                    flags=0x0,
                    OS=0x4,
                    fileType=0x1,
                    subtype=0x0,
                    date=(0, 0)
                ),
                kids=[
                    StringFileInfo(
                        [
                            StringTable(
                                u'040904B0',
                                [StringStruct(u'CompanyName', u'{strAuthor}'),
                                StringStruct(u'FileDescription', u'{strName}'),
                                StringStruct(u'FileVersion', u'{tupleVersion}'),
                                StringStruct(u'InternalName', u'{strName.upper()}'),
                                StringStruct(u'LegalCopyright',
                                            u'Copyright (c) {strAuthor}'),
                                StringStruct(u'OriginalFilename', u'{strName}.exe'),
                                StringStruct(u'ProductName', u'{strName}'),
                                StringStruct(u'ProductVersion', u'{strVersion}')])
                        ]),
                    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
                ]
            )""")
        print(f"{Fore.BLUE}Writing {strVersionFile} Done")
    except:
        print(f"{Fore.RED}Failed writing {strVersionFile}")
