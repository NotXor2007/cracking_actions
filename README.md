# cracking-actions 0.9 Alpha
### zip cracker supports ![Static Badge](https://img.shields.io/badge/Deflate-blue) ![Static Badge](https://img.shields.io/badge/Deflate64-blue) ![Static Badge](https://img.shields.io/badge/Bzip2-blue) ![Static Badge](https://img.shields.io/badge/LZMA-blue) 
### cracking-actions is an open source software for cracking passwords, files, etc...
## requirements:
#### windows 7 or later
## Installation guide:
#### you can install a binary release from github or by visiting sourceforge or mediafire.
#### you will need 7zip or winrar or any program capable of extracting zip file to extract it
#### finally run cracking-actions executable file
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
#### and you need also to compile the AutoCreator.bas which is found in <u>core</u> directory using fbc.exe, so you need to install FreeBasic compiler finally to get AutoCreator executable file
### here is how to do that
navigate to the core directory and then type in console
`fbc AutoCreator.bas`
### Note:of course you need to add fbc to path or simply write the full path to fbc
#### and finally you can build the project by typing the following in the console in the repo directory
`pyinstaller --onefile --icon <icon-path> <'cracking-actions.py' file path>`
#### after this you should get a dist directory where the exe should, simply now copy the lang and the icon and the core directories to the dist dir and leave in the core dir AutoCreator executable and copy to it an external file which is unrar.exe you can get it from the binary release
## To Do
- [ ] add support to multiprocessing to speed up cracking process
- [ ] add to zip cracker support to PPMd compression method
- [ ] add AES-256 encryption method support
- [ ] write the core in a compiled language (FreeBasic)
- [ ] add language support to console
- [ ] add website enumeration tool
- [ ] add wifi cracker tool

## Done
- [x] support for saving progress and loading it later
- [x] support for Deflate64 was added to zip cracker
- [x] support for wordlist was added
- [x] settings menu was added
- [x] rar cracker was added
- [x] build for windows
- [x] gui interface was added
- [x] hash password cracker was added
- [x] zip file cracker was added
### Note: the linux build is coming soon!
### ⚠️ for educational purposes only!
### ©2023-2025 preprocessed NotXor2007.All rights reserved.
