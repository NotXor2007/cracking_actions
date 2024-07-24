#a password cracker by adam naanaa
#finished in 05/07/2024 at 7:44PM  
#importing libraries
import sys, os, platform
import colorama
from colorama import Fore
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from const import*
from engine import*
from widgets.menu import MenuBar
from widgets.pswdatk import AttackPswd 
from widgets.zipatk import AttackZip
from widgets.output import OutputTerm
from man import Manual

cdate = "©ADAM-TECH 10/07/2024"

class Window:

	def __init__(self, w, h, title, bg, commands_list, types_list):
		S = Start(self)
		self.w, self.h = w, h
		self.title = title
		self.bg = bg
		self.window = tk.Tk()
		self.window.title(title)
		self.window.configure(background="#"+self.bg)
		self.window.resizable(False, False)
		self.window.wm_attributes("-topmost", True)
		self.window.geometry(f"{self.w}x{self.h}")
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.__menu()
		self.__wsetup(commands_list, types_list, S)
		self.pswdatk()
		self.__draw()
		self.update()

	def __wsetup(self, commands_list, types_list, S):
		self.pswdattack = AttackPswd(self.window)
		self.pswdattack.attackAlgo(commands_list)
		self.pswdattack.attackType(types_list)
		self.pswdattack.hashedKey()
		self.pswdattack.lengthKey()
		self.pswdattack.start_btn(S)
		self.pswdattack.stop_btn()
		self.zipattack = AttackZip(self.window)
		self.zipattack.attackAlgo(commands_list)
		self.zipattack.lengthKey()
		self.zipattack.fileIn()
		self.zipattack.fileOut()
		self.zipattack.start_btn(S)
		self.zipattack.stop_btn()
		self.out = OutputTerm(self.window)
		self.out.output()
		self.pswdattack.pack()
		self.zipattack.pack()
		self.out.pack()

	def __draw(self):
		self.pswdattack.frame.grid(row=0, column=0, columnspan=1, sticky="nesw")
		self.zipattack.frame.grid(row=0, column=1, columnspan=1, sticky="nwse")
		self.out.frame.grid(row=1, column=0, columnspan=2, sticky="sew")

	def __menu(self):
		menu = MenuBar(self.window, self.on_closing, self.get_help, 
			self.pswdatk, self.zipatk, self.mwin)

	def on_closing(self):
		result = messagebox.askokcancel("Are you sure?", "Do you want to close cracking actions v0.7")
		if result:
			sys.exit(0)
		else:
			pass

	def get_help(self):
		windowc = "#000022"
		help_window = tk.Toplevel(self.window)
		help_window.wm_attributes("-topmost", True)
		help_window.resizable(False, True)
		help_window.geometry("870x400")
		help_window.configure(bg=windowc)
		help_window.wm_attributes("-alpha", 0.85)
		help_window.title("cracking actions v0.7-help")
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
		about_window.title("cracking actions v0.7-About")
		tk.Label(about_window, text="cracking actions v0.7",
			background=windowc,foreground="#ffff88", font="Times 25 bold").pack()
		tk.Label(about_window, text="a software that allows you to crack password, files etc...",
			background=windowc,foreground="#AABBFF", font="Helvetica 15 bold").pack()
		tk.Label(about_window, text="developped and published by adam naanaa",
			background=windowc,foreground="#AABBFF", font="Helvetica 15 bold").pack()
		tk.Label(about_window, text=cdate,
			background=windowc,foreground="#AA55AA", font="Times 20 bold").pack()	

	def pswdatk(self):
		for child in self.zipattack.frame.winfo_children():
			child.configure(state="disabled")
		for child in self.pswdattack.frame.winfo_children():
			child.configure(state="active")

	def zipatk(self):
		for child in self.pswdattack.frame.winfo_children():
			child.configure(state="disabled")	
		for child in self.zipattack.frame.winfo_children():
			child.configure(state="active")	

	def readraw(self):
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
		print(Fore.RED + " ▄▄· ▄▄▄   ▄▄▄·  ▄▄· ▄ •▄ ▪   ▐ ▄  ▄▄ •      ▄▄▄·  ▄▄· ▄▄▄▄▄▪         ▐ ▄ .▄▄ ·") 
		print("▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▌▪█▌▄▌▪██ •█▌▐█▐█ ▀ ▪    ▐█ ▀█ ▐█ ▌▪•██  ██ ▪     •█▌▐█▐█ ▀.") 
		print("██ ▄▄▐▀▀▄ ▄█▀▀█ ██ ▄▄▐▀▀▄·▐█·▐█▐▐▌▄█ ▀█▄    ▄█▀▀█ ██ ▄▄ ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄")
		print("▐███▌▐█•█▌▐█ ▪▐▌▐███▌▐█.█▌▐█▌██▐█▌▐█▄▪▐█    ▐█ ▪▐▌▐███▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█")
		print("·▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ ·▀  ▀▀▀▀▀▀ █▪·▀▀▀▀      ▀  ▀ ·▀▀▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀ ")
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
		cmd = input(Fore.BLUE + "Command:")
		algo = input("Algorithm:")
		hashedkey = input("Hash:")
		mgl = input("Mgl:")	
		S.attackHash(algo, hashedkey,
			mgl, self.__getOption(cmd), cli=True)

	def __runzipatk(self, S):
		Start.STOPZIP = False
		cmd = input(Fore.BLUE + "Command:")
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

		elif Cli.ATKTYPE == 1:
			print("pswdattack commands:")
			print("++++zipattack ==> switch to zip cracker page++++")
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

	def __execute(self, S):
		if Cli.ATKTYPE == 0:
			cmd = input(Fore.GREEN + "==>")
		elif Cli.ATKTYPE == 1:
			cmd = input(Fore.GREEN + "==>pswdattack==>")
		elif Cli.ATKTYPE == 2:
			cmd = input(Fore.GREEN + "==>zipattack==>")
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
			self.__get_page()
		elif cmd.lower().strip() == "":
			pass
		elif cmd.lower() == "exit" or cmd.lower() == "quit":
			self.__on_closing()
		else:
			print(Fore.WHITE + "unknown command!")

	def __on_closing(self):
		result = messagebox.askokcancel("Are you sure?", "Do you want to close cracking actions v0.7")
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
	if check_man():
		Manual("cracking actions v0.7", commands_list, available_types)
	elif check_cli():
		Cli("cracking actions v0.7", commands_list, available_types)
	else:
		Window(653,575,"cracking actions v0.7","555555", commands_list, available_types)
