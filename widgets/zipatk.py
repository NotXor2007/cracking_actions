import tkinter as tk
from tkinter import ttk
from supercls import Widgets
from core.engine import*
import threading
from const import*
from tkinter import messagebox
from tkinter import filedialog

class AttackZip(Widgets):

	def __init__(self, window):
		Widgets.__init__(self, window)
		self.frame = tk.LabelFrame(self.window,text="attack zipfile",borderwidth=4,relief="groove")
		self.file_path, self.file_output="", ""

	def attackAlgo(self, commands_list):
		self.Commandtype = tk.Label(self.frame,text="Command:")
		self.attackAlgoW = ttk.Combobox(self.frame)
		options = commands_list
		self.attackAlgoW["values"] = options
		self.attackAlgoW.set(self.attackAlgoW["values"][0])

	def lengthKey(self):
		self.Ltype = tk.Label(self.frame,text="Mgl:")
		self.lengthkey = ttk.Entry(self.frame)
		self.lengthkey.insert(0, "max generated length")

	def __pathIn(self):
		self.file_path = filedialog.askopenfilename(title="select a zipfile",
			filetypes=[("zipfile", ".zip")])
		if not self.file_path == "":
			self.FileIE.delete(0, tk.END)
			self.FileIE.insert(tk.END, self.file_path)

	def __pathOut(self):
		self.file_output = filedialog.askdirectory(title="choose output dir")
		if not self.file_output == "":
			self.FileOutE.delete(0, tk.END)
			self.FileOutE.insert(tk.END, self.file_output)

	def fileIn(self):
		self.FItype = tk.Label(self.frame,text="file path:")
		self.FileIE = ttk.Entry(self.frame)
		self.fibtn = tk.Button(self.frame,text="select file",
			command=lambda :self.__pathIn())

	def fileOut(self):
		self.FOuttype = tk.Label(self.frame,text="output path:")
		self.FileOutE = ttk.Entry(self.frame)
		self.foutbtn = tk.Button(self.frame,text="choose output",
			command=lambda :self.__pathOut())


	def __getOption(self):
		option = self.attackAlgoW.get()
		for o in zip(commands_list, char_options):
			if o[0] == option:
				return o[1]
			else:
				continue

	def __start_btn_cmd(self, S):
		if not Start.STOPZIP:
			result = messagebox.showwarning("Warning", "the attack is already running!")
		else:
			Start.STOPZIP = False
			self.task = threading.Thread(target=S.attackZip, args=(
				self.file_path,self.file_output,self.lengthkey.get(),self.__getOption()))
			self.task.start()

	def __stop_btn_cmd(self):
		Start.STOPZIP = True

	def start_btn(self, S):
		self.stabtn = tk.Button(self.frame,text="start attack",
			command=lambda :self.__start_btn_cmd(S))

	def __help(self):
		self.menu_bar.add_command(label="help", command = self.get_help)

	def stop_btn(self):
		self.stobtn = tk.Button(self.frame,text="stop attack",
			command=self.__stop_btn_cmd)

	def pack(self):
		#-------------------------------------
		self.Commandtype.grid(row=0, column=0, sticky="w")
		self.attackAlgoW.grid(row=0, column=1, sticky="w")
		#-------------------------------------
		self.Ltype.grid(row=3, column=0, sticky="w")
		self.lengthkey.grid(row=3, column=1, sticky="w")
		#-------------------------------------
		self.FItype.grid(row=4, column=0, sticky="w")
		self.FileIE.grid(row=4, column=1, sticky="w")
		self.fibtn.grid(row=4, column=2, sticky="w")
		#-------------------------------------
		self.FOuttype.grid(row=5, column=0, sticky="w")
		self.FileOutE.grid(row=5, column=1, sticky="w")
		self.foutbtn.grid(row=5, column=2, sticky="w")
		#-------------------------------------
		self.stabtn.grid(row=6, column=0, columnspan=3, sticky="ew")
		self.stobtn.grid(row=7, column=0, columnspan=3, sticky="ew")
