# cracking-actions ![Static Badge](https://img.shields.io/badge/cracking--actions%20alpha%200.8-red) ![GitHub Downloads (specific asset, latest release)]
### cracking-actions is an open source software that allows you to crack passwords, files, etc... also it's available on windows and linux
## requirements:
#### windows 7 or later
## Installation guide:
#### you can install a binary release from github or by visiting sourceforge or mediafire.
#### you will need 7zip or winrar or any program capable of extracting zip file to extract it
#### finally run cracking-actions alpha 0.8 executable file
## Building from source:
clone the repository
`git clone https://github.com/NotXor2007/cracking_actions.git`
#### you will need to install python interpreter and then install the requirements using this command
`pip install -r requirements.txt`
### Note:it's recommanded to create a virtual environment for the project using this command in the console
`python -m venv venv`
#####
here is how to use the virtual environment on windows
`.\venv\scripts\activate.bat`
#### here is how to do it on linux
#### and you need also to compile the AutoCreaotr.bas which is found in <u>core</u> directory using fbc.exe, so you need to install FreeBasic compiler finally to get AutoCreator executable file
### here is how to do that
navigate to the core directory and then type in console
`fbc AutoCreator.bas`
### Note:of coure you need to add fbc to path or simply write the full path to fbc
#### and finally you can build the project by typing thz following in the console in the repo directory
`pyinstaller --onefile --icon [icon-path] [cracking-actions.py file]`
#### after this you should get a dist directory where the exe should, simply now copy the lang and the icon and the core directories to the dist dir and leave in the core dir AutoCreator executable and copy to it an external file which is unrar.exe you can get it from the binary release
## To Do
- [ ] adding to zip cracker support to Deflate64, PPMd compression methods
- [ ] adding AES-256 encryption method support
- [ ] add language support in console
- [ ] adding website enumeration tool
- [ ] adding wifi cracker tool

## Done
- [x] adding support for wordlist
- [x] adding settings menu
- [x] adding rar cracker
- [x] compile for linux and windows
- [x] adding gui interface
- [x] adding hash password cracker
- [x] adding zip file cracker
### ©2023-2025 preprocessed NotXor2007.All rights reserved.
