#a password cracker by NotXor2007
#finished in 
#importing libraries
import sys, os, platform
import colorama
from colorama import Fore
import tkinter as tk
from tkinter import ttk
from win32ui import MessageBox
from win32con import*
from tkinter import scrolledtext
from tkinter import filedialog
from const import*
from core.engine import*
from widgets.settings import Settings
from widgets.menu import MenuBar
from widgets.pswdatk import AttackPswd 
from widgets.zipatk import AttackZip
from widgets.raratk import AttackRar
from widgets.output import OutputTerm
from widgets.shell import Shell
from man import Manual
from core import cfghandler

#f"" not supported on windows xp------

class Window:

	def __init__(self, w, h, title, bg, commands_list, types_list, language):
		S = Start(self)
		self.w, self.h = w, h
		self.title = title
		self.bg = bg
		self.wlist = None
		self.language = language
		self.window = tk.Tk()
		self.wsettings = Settings(self, self.window, self.language)
		self.window.title(title)
		self.window.configure(background="#"+self.bg)
		self.window.iconbitmap(icon)
		self.window.resizable(False, False)
		self.window.wm_attributes("-topmost", False)
		self.redraw()
		self.window.geometry(f"{self.w}x{self.h}+0+0")
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.__menu()
		self.__wsetup(commands_list, types_list, S)
		self.__shell_enabler()
		self.pswdatk()
		self.__draw()
		self.pswdattack.attackAlgoW.config(state="readonly")
		self.pswdattack.attackTypeW.config(state="readonly")
		self.window.geometry(f"+{sc_width//2-self.w//2}+{sc_height//2-self.h//2}")
		self.update()

	def __wsetup(self, commands_list, types_list, S):
		#set up password attacker gui
		self.pswdattack = AttackPswd(self, self.window)
		self.pswdattack.attackAlgo(commands_list)
		self.pswdattack.attackType(types_list)
		self.pswdattack.hashedKey()
		self.pswdattack.lengthKey()
		self.pswdattack.start_btn(S)
		self.pswdattack.stop_btn()
		#set up zip attacker gui
		self.zipattack = AttackZip(self, self.window)
		self.zipattack.attackAlgo(commands_list)
		self.zipattack.lengthKey()
		self.zipattack.fileIn()
		self.zipattack.fileOut()
		self.zipattack.start_btn(S)
		self.zipattack.stop_btn()
		#set up rar attacker gui
		self.rarattack = AttackRar(self, self.window)
		self.rarattack.attackAlgo(commands_list)
		self.rarattack.lengthKey()
		self.rarattack.fileIn()
		self.rarattack.fileOut()
		self.rarattack.start_btn(S)
		self.rarattack.stop_btn()
		#set up output attacker gui
		self.out = OutputTerm(self, self.window)
		self.out.output()
		#pack gui
		self.pswdattack.pack()
		self.zipattack.pack()
		self.rarattack.pack()
		self.out.pack()
	#basically makes the shell works
	def __shell_enabler(self):
		shell = Shell(self)

	def __draw(self):
		#draw gui frame
		tk.Grid.columnconfigure(self.window, 0, weight=1)
		tk.Grid.columnconfigure(self.window, 1, weight=1)
		tk.Grid.columnconfigure(self.window, 2, weight=1)
		tk.Grid.rowconfigure(self.window, 0, weight=1)

		self.pswdattack.frame.grid(row=0, column=0, columnspan=1, sticky="nesw")
		self.zipattack.frame.grid(row=0, column=1, columnspan=1, sticky="nwse")
		self.rarattack.frame.grid(row=0, column=2, columnspan=1, sticky="nwse")
		self.out.frame.grid(row=1, column=0, columnspan=3, sticky="sew")
	#create menu
	def __menu(self):
		menu = MenuBar(self, self.window, self.on_closing, self.get_help, 
			self.pswdatk, self.zipatk, self.raratk, self.load_wlst, self.settings, self.mwin)

	def on_closing(self):
		if MessageBox(self.language[10], self.language[9], MB_YESNO | MB_ICONQUESTION) == 6:
			sys.exit(0)

	def get_help(self):
		windowc = "#000022"
		help_window = tk.Toplevel(self.window)
		help_window.wm_attributes("-topmost", True)
		help_window.resizable(False, True)
		help_window.geometry("870x400")
		help_window.configure(bg=windowc)
		help_window.iconbitmap(icon)
		help_window.wm_attributes("-alpha", 0.85)
		help_window.title(self.language[21])
		scroll = scrolledtext.ScrolledText(help_window,width=950,
			height=600, bg=windowc, wrap=tk.WORD)
		scroll.pack()
		scroll.tag_configure("toptions", background=windowc,
			foreground="#ffff00",font="Helvetica 30 bold")
		scroll.tag_configure("center", justify='center')
		scroll.insert(tk.INSERT,"Usage\n")
		scroll.tag_add("toptions", "1.0", "1.end")
		scroll.tag_add("center", "1.0", "1.end")
		scroll.tag_configure("cmdoptions", background=windowc,
			foreground="#ffffff",font="Helvetica 14 bold")
		for cmd in commands_list_man:
			index = commands_list_man.index(cmd)
			scroll.insert(tk.INSERT,cmd+"\n")
			scroll.tag_add("cmdoptions", str(index+2.0), str(index+2)+".end")

	def mwin(self):
		windowc = "#000000"
		about_window = tk.Toplevel(self.window)
		about_window.wm_attributes("-topmost", True)
		about_window.wm_attributes("-alpha", 0.85)
		about_window.resizable(False, False)
		about_window.geometry("600x160")
		about_window.configure(bg=windowc)
		about_window.iconbitmap(icon)
		about_window.title(self.language[11])
		tk.Label(about_window, text="cracking actions v0.8",
			background=windowc,foreground="#ffff88", font="Times 25 bold").pack()
		tk.Label(about_window, text=self.language[12],
			background=windowc,foreground="#AABBFF", font="Helvetica 13 bold").pack()
		tk.Label(about_window, text=self.language[13],
			background=windowc,foreground="#AABBFF", font="Helvetica 15 bold").pack()
		tk.Label(about_window, text=cdate,
			background=windowc,foreground="#AA55AA", font="Times 13 bold").pack()	
	#creating menu events
	def pswdatk(self):
		for child in self.zipattack.frame.winfo_children():
			child.configure(state="disabled")
		for child in self.pswdattack.frame.winfo_children():
			child.configure(state="active")
		for child in self.rarattack.frame.winfo_children():
			child.configure(state="disabled")
		self.pswdattack.attackAlgoW.config(state="readonly")
		self.pswdattack.attackTypeW.config(state="readonly")

	def zipatk(self):
		for child in self.pswdattack.frame.winfo_children():
			child.configure(state="disabled")	
		for child in self.zipattack.frame.winfo_children():
			child.configure(state="active")
		for child in self.rarattack.frame.winfo_children():
			child.configure(state="disabled")
		self.zipattack.attackAlgoW.config(state="readonly")

	def raratk(self):
		for child in self.pswdattack.frame.winfo_children():
			child.configure(state="disabled")	
		for child in self.zipattack.frame.winfo_children():
			child.configure(state="disabled")
		for child in self.rarattack.frame.winfo_children():
			child.configure(state="active")
		self.rarattack.attackAlgoW.config(state="readonly")	

	def load_wlst(self):
		file_path = filedialog.askopenfilename(title=self.language[50],
			filetypes=[(self.language[51], ".txt")])
		if file_path != "":
			with open(file_path, "r", encoding="utf-8") as wlist:
				self.wlist = wlist.readlines()
			for word in self.wlist:
				self.wlist[self.wlist.index(word)] = word.rstrip("\n")
			commands_list.append(file_path)
			self.pswdattack.attackAlgoW["values"]= commands_list
			self.zipattack.attackAlgoW["values"]= commands_list
			self.rarattack.attackAlgoW["values"]= commands_list
			commands_list.remove(commands_list[-1])
			self.out.console.insert(tk.END, "%s %s\n"%(self.language[52],file_path))

	def settings(self):
		self.wsettings.show_settings()

	def redraw(self):
		self.window.update_idletasks()

	def Aupdate(self):
		self.window.update()

	def update(self):
		self.window.mainloop()

class Cli:
	ATKTYPE = 0
	def __init__(self, title, commands_list, types_list):
		colorama.init()
		S = Start(self)
		Start.STOPPSWD = False
		Start.STOPZIP = False
		#not supported on windows xp-----------
		print(Fore.RED + " ▄▄· ▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ •      ▄▄▄·  ▄▄· ▄▄▄▄▄▪         ▐ ▄ .▄▄ ·") 
		print("▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪    ▐█ ▀█ ▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀.") 
		print("██ ▄▄▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄    ▄█▀▀█ ██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄")
		print("▐███▌▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█    ▐█ ▪▐▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█")
		print("·▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀      ▀  ▀ ·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀ ")
                #--------------------------------------
		print(Fore.GREEN + "----------"+title+"----------")
		print("a software that allows you to crack password, files etc...")
		print("---developped and published by adam naanaa---")
		print("----------" + cdate + "----------")
		print(Fore.WHITE + "please enter help for help")
		while True:
			self.__execute(S)

	def __getOption(self, option):
		for o in zip(commands_list, char_options):
			if o[0] == option:
				return o[1]
			else:
				continue

	def __runpswdatk(self, S):
		Start.STOPPSWD = False
		print(Fore.BLUE, end = "")
		cmd = input("Command:")
		algo = input("Algorithm:")
		hashedkey = input("Hash:")
		mgl = input("Mgl:")	
		S.attackHash(algo, hashedkey,
			mgl, self.__getOption(cmd), cli=True)

	def __runzipatk(self, S):
		Start.STOPZIP = False
		print(Fore.BLUE, end = "")
		cmd = input("Command:")
		mgl = input("Mgl:")
		fpath = input("file path:")
		opath = input("output path:")
		S.attackZip(fpath,opath,mgl,self.__getOption(cmd),cli=True)

	def __not_available(self):
		print(Fore.WHITE + "command not available!")

	def __get_page(self):
		if Cli.ATKTYPE == 0:
			print(Fore.WHITE + "main")
		elif Cli.ATKTYPE == 1:
			print("pswdattack")
		elif Cli.ATKTYPE == 2:
			print("zipattack")		

	def __help(self):
		print(Fore.WHITE + "------------Usage------------")
		print("universal commands:")
		print("++++exit or quit ==> exit++++")
		print("++++help ==> for help++++")
		print("++++clear ==> clear the console++++")
		print("++++gcp ==> get current page++++")
		if Cli.ATKTYPE == 0:
			print("main commands:")
			print("++++pswdattack ==> switch password cracker page(hash only!)++++")
			print("++++zipattack ==> switch to zip cracker page++++")
			print("++++rarattack ==> switch to rar cracker page++++")

		elif Cli.ATKTYPE == 1:
			print("pswdattack commands:")
			print("++++zipattack ==> switch to zip cracker page++++")
			print("++++rarattack ==> switch rar cracker page++++")
			print("++++main ==> switch to main page++++")
			print("password attacker:") 
			print("++++commands++++")
			for _ in commands_list_man:
				print("++++-----"+_+"-----++++")
			print("++++Algorithms++++")
			for _ in available_types:
				print("++++-----"+_+"-----++++")
			print("++++Hash++++")
			print("++++----provide a key to decrypt----++++")
			print("++++Mgl++++")
			print("++++----maximum generated length----++++")
		elif Cli.ATKTYPE == 2:
			print("zipattack commands:")
			print("++++pswdattack ==> switch password cracker page(hash only!)++++")
			print("++++rarattack ==> switch rar cracker page++++")
			print("++++main ==> switch to main page++++")
			print("zip attacker:") 
			print("++++commands++++")
			for _ in commands_list_man:
				print("++++-----"+_+"-----++++")
			print("++++Mgl++++")
			print("++++----maximum generated length----++++")
			print("++++path++++")
			print("++++----provide path to the zip file----++++")
			print("++++output++++")
			print("++++----provide path to the extracted data----++++")
		elif Cli.ATKTYPE == 3:
			print("rarattack commands:")
			print("++++pswdattack ==> switch password cracker page(hash only!)++++")
			print("++++zipattack ==> switch to zip cracker page++++")
			print("++++main ==> switch to main page++++")
			print("rar attacker:") 
			print("++++commands++++")
			for _ in commands_list_man:
				print("++++-----"+_+"-----++++")
			print("++++Mgl++++")
			print("++++----maximum generated length----++++")
			print("++++path++++")
			print("++++----provide path to the zip file----++++")
			print("++++output++++")
			print("++++----provide path to the extracted data----++++")

	def __execute(self, S):
		#check for selected attacker
		if Cli.ATKTYPE == 0:
			print(Fore.GREEN, end = "")
			cmd = input("==>")
		elif Cli.ATKTYPE == 1:
			print(Fore.GREEN, end = "")
			cmd = input("==>pswdattack==>")
		elif Cli.ATKTYPE == 2:
			print(Fore.GREEN, end = "")
			cmd = input("==>zipattack==>")
		elif Cli.ATKTYPE == 3:
			print(Fore.GREEN, end = "")
			cmd = input("==>rarattack==>")

		if cmd.lower() == "help":
			self.__help()
		elif cmd.lower() == "pswdattack":
			if not Cli.ATKTYPE == 1:
				print(Fore.WHITE + "welcome to password cracker")
				Cli.ATKTYPE = 1
			else:
				self.__not_available()
		elif cmd.lower() == "zipattack":
			if not Cli.ATKTYPE == 2:
				print(Fore.WHITE + "welcome to zip cracker")
				Cli.ATKTYPE = 2
			else:
				self.__not_available()
		elif cmd.lower() == "rarattack":
			if not Cli.ATKTYPE == 3:
				print(Fore.WHITE + "welcome to rar cracker")
				Cli.ATKTYPE = 3
			else:
				self.__not_available()
		elif cmd.lower() == "main":
			if not Cli.ATKTYPE == 0:
				Cli.ATKTYPE = 0
			else:
				self.__not_available()
		elif cmd.lower() == "run" and Cli.ATKTYPE == 1:
			self.__runpswdatk(S)
		elif cmd.lower() == "run" and Cli.ATKTYPE == 2:
			self.__runzipatk(S)
		elif cmd.lower() == "clear":
			if platform.system() == "Windows":
				os.system("cls")
			elif platform.system() == "Linux":
				os.system("clear")
		elif cmd.lower() == "gcp":
                        print(Fore.WHITE, end = "")
                        self.__get_page()
		elif cmd.lower().strip() == "":
			pass
		elif cmd.lower() == "exit" or cmd.lower() == "quit":
			self.__on_closing()
		else:
			print(Fore.WHITE + "unknown command!")

	def __on_closing(self):
		result = messagebox.askokcancel("Are you sure?", "Do you want to close cracking actions v0.8")
		if result:
			sys.exit(0)
		else:
			pass

def check_cli():
	argvs = sys.argv
	if len(argvs) == 1:
		return False
	elif len(argvs) > 1:
		if argvs[1] == "-cli":
			return True
		elif argvs[1] == "-gui":
			return False
	return False

def check_man():
	argvs = sys.argv
	if len(argvs) == 1:
		return False
	elif len(argvs) > 1:
		if argvs[1] == "-man":
			return True
		elif argvs[1] == "-cli":
			return False
		elif argvs[1] == "-gui":
			return False
	return False

if __name__ == "__main__":
	if platform.architecture()[0] == "32it":
		MessageBox("failed to run because you aren't on a 64-bit machine","Exit with Failure",MB_OK|MB_ICONERROR)
		sys.exit(-1)
	if not os.path.exists(".\\settings.cfg"):
		subp = __import__("subprocess")
		subp.run([".\\core\\AutoCreator.exe", "--settings"], shell = True)
		language = cfghandler.readcfg()
	else:
		language = cfghandler.readcfg() #TODO:take car of return exceptions
	if check_man():
		Manual("cracking actions v0.8", commands_list, available_types)
	elif check_cli():
		Cli("cracking actions v0.8", commands_list, available_types)
	else:
		Window(840,622,"cracking actions v0.8","555555", commands_list, available_types, language)
