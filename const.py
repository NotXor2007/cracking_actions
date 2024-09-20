import string
import rarfile
import ctypes
import platform

if platform.system().lower() == "windows":
	rarfile.UNRAR_TOOL = ".\\core\\unrar.exe"
	icon = ".\\icon\\cracking-actions-icon.ico"
	settingsfile = ".\\settings.cfg"
	AutoCreator = ".\\core\\AutoCreator.exe"
	sc_width = ctypes.windll.user32.GetSystemMetrics(0)
	sc_height = ctypes.windll.user32.GetSystemMetrics(1)
elif platform.system().lower() == "linux":
	pass #TODO

cdate = "©2023-2025 preprocessed NotXor2007.All rights reserved.20/09/2024"

available_types = ["md5","sha1","sha224","sha384","sha3_224","sha3_512","sha3_384","sha3_256","sha256","sha512","blake2b","blake2s"]

char_options = (string.digits,string.ascii_lowercase,string.ascii_uppercase
,string.ascii_lowercase+string.digits,string.ascii_uppercase+string.digits
,string.ascii_letters,string.ascii_letters+string.digits,string.punctuation
,string.punctuation+string.digits,string.punctuation+string.ascii_lowercase
,string.punctuation+string.ascii_uppercase
,string.punctuation+string.ascii_lowercase+string.digits
,string.punctuation+string.ascii_uppercase+string.digits
,string.punctuation+string.ascii_letters
,string.punctuation+string.ascii_letters+string.digits
,string.digits,string.ascii_lowercase,string.ascii_uppercase
,string.ascii_lowercase+string.digits,string.ascii_uppercase+string.digits
,string.ascii_letters,string.ascii_letters+string.digits,string.punctuation
,string.punctuation+string.digits+" ",string.punctuation+string.ascii_lowercase+" "
,string.punctuation+string.ascii_uppercase+" "
,string.punctuation+string.ascii_lowercase+string.digits+" "
,string.punctuation+string.ascii_uppercase+string.digits+" "
,string.punctuation+string.ascii_letters+" "
,string.punctuation+string.ascii_letters+string.digits+" ")

commands_list = ["start -n","start -cl", "start -cu", "start -cl -n", 
"start -cu -n", "start -cu -cl", "start -cu -cl -n", "start -s", "start -s -n",
"start -s -cl", "start -s -cu", "start -s -cl -n", "start -s -cu -n", 
"start -s -cu -cl", "start -s -cu -cl -n", "start -sp -n", "start -sp -cl",
"start -sp -cu", "start -sp -cl -n", "start -sp -cu -n", "start -sp -cu -cl",
"start -sp -cu -cl -n", "start -sp -s", "start -sp -s -n", "start -sp -s -cl",
"start -sp -s -cu", "start -sp -s -cl -n", "start -sp -s -cu -n", 
"start -sp -s -cu -cl", "start -sp -s -cu -cl -n"]

commands_list_man = ("start -n: to use password cracker only for numbers",
	"start -cl: to use it only for lowercase letters", 
	"start -cu: to use it for uppercase letters", 
	"start -cl -n: to use it for both numbers and lowercase letters", 
"start -cu -n: to use it for both numbers and uppercase letters", 
"start -cu -cl:to use it for both lowercase and uppercase", 
"start -cu -cl -n: to use it for all", 
"start -s: to use password cracker only for special char", 
"start -s -n: to use password cracker for numbers and special char",
"start -s -cl: to use it for lowercase letters and special char", 
"start -s -cu: to use it for uppercase letters and special char", 
"start -s -cl -n: to use it for both numbers,lowercase letters and special char", 
"start -s -cu -n: to use it for both numbers,uppercase letters and special char", 
"start -s -cu -cl:to use it for both lowercase and uppercase and special char", 
"start -s -cu -cl -n: to use it for all with special char", 
"start -sp -n: to use password cracker only for numbers with space", 
"start -sp -cl: to use it only for lowercase letters with space",
"start -sp -cu: to use it for uppercase letters with space", 
"start -sp -cl -n: to use it for both numbers and lowercase letters with space", 
"start -sp -cu -n: to use it for both numbers and uppercase letters with space", 
"start -sp -cu -cl:to use it for both lowercase and uppercase with space",
"start -sp -cu -cl -n: to use it for all with space", 
"start -sp -s: to use password cracker only for special char with space", 
"start -sp -s -n: to use password cracker for numbers and special char with space", 
"start -sp -s -cl: to use it for lowercase letters and special char with space",
"start -sp -s -cu: to use it for uppercase letters and special char with space", 
"start -sp -s -cl -n: to use it for both numbers,lowercase letters and special char with space", 
"start -sp -s -cu -n: to use it for both numbers,uppercase letters and special char with space", 
"start -sp -s -cu -cl:to use it for both lowercase and uppercase and special char with space", 
"start -sp -s -cu -cl -n: to use it for all and special char with space")
