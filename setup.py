import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os" ], "excludes": [], "include_msvcr": 1}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
elif sys.platform == "win64":
    base = "Win64GUI"
else:
    base = None

            
            

setup(  name = "NationalNumberKnockout",
        version = "0.1",
        description = "Solves NNK boards",
        options = {"build_exe": build_exe_options},
        executables = [Executable("MainScreen.py", base=base)])
