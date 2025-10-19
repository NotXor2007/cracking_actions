#a password cracker by NotXor2007
#finished in 
#importing libraries
import sys, os, platform
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
from widgets.hashatk import AttackPswd 
from widgets.zipatk import AttackZip
from widgets.raratk import AttackRar
from widgets.output import OutputTerm
from widgets.shell import Shell
from man import Manual
from core import cfghandler

#f""is not supported on windows xp------

class Window:

	def __init__(self, title, bg, commands_list, types_list, language):
		S = Start(self)
		self.w, self.h = None, None
		self.title = title
		self.bg = bg
		self.wlist = None
		self.language = language
		self.window = tk.Tk()
		self.wsettings = Settings(self, self.window, self.language)
		self.window.title(title)
		self.window.configure(background="#"+self.bg)
		self.window.iconbitmap(icon)
		self.window.resizable(True, True)
		self.window.wm_attributes("-topmost", False)
		self.__setwindowmin()
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
		self.window.geometry(f"+{sc_width//2-self.w//2}+{(sc_height//2-self.h//2)-10}")
		self.update()
		
        #setup window smallest size
	def __setwindowmin(self):
		if self.language[0].lower() == "english":
			self.window.wm_minsize(840,610)
			self.w, self.h = 840, 610
		elif self.language[0].lower() == "francais":
			self.window.wm_minsize(1000,610)
			self.w, self.h = 1000, 610
		elif self.language[0].lower() == "عربية":
			self.window.wm_minsize(760,610)
			self.w, self.h = 760, 610

        #setup widgets
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
		
	#basically makes the shell work
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

        #show close dialog
	def on_closing(self):
		if MessageBox(self.language[10], self.language[9], MB_YESNO | MB_ICONQUESTION) == 6:
			sys.exit(0)

        #show help window
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

        #show about window
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
		tk.Label(about_window, text="cracking actions v0.9",
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
		file = filedialog.askopenfile(title=self.language[50],
			filetypes=[(self.language[51], ".txt")])
		if file != None:
			self.wlist = file.readlines()
			for word in self.wlist:
				self.wlist[self.wlist.index(word)] = word.rstrip("\n")
			commands_list.append(file.name)
			self.pswdattack.attackAlgoW["values"]= commands_list
			self.zipattack.attackAlgoW["values"]= commands_list
			self.rarattack.attackAlgoW["values"]= commands_list
			commands_list.remove(commands_list[-1])
			self.out.console.insert(tk.END, "%s %s\n"%(self.language[52],file.name))

	def settings(self):
		self.wsettings.show_settings()

	def redraw(self):
		self.window.update_idletasks()

	def Aupdate(self):
		self.window.update()

	def update(self):
		self.window.mainloop()

if __name__ == "__main__":
	if platform.architecture()[0] == "32it":
		MessageBox("failed to run because you aren't on a 64-bit machine","Exit with Failure",MB_OK|MB_ICONERROR)
		sys.exit(-1)
	if not os.path.exists(settingsfile):
		cfghandler.createcfg()
		language = cfghandler.readcfg()
	else:
		language = cfghandler.readcfg() #TODO:take care of return exceptions
		if language == -1:
			cfghandler.createcfg()
			language = cfghandler.readcfg()
	Window("cracking actions v0.9","555555", commands_list, available_types, language)
