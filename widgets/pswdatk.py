import tkinter as tk
from tkinter import ttk
from supercls import Widgets
from core.engine import*
import threading
from const import*
from tkinter import messagebox

class AttackPswd(Widgets):

	def __init__(self, win, window):
		Widgets.__init__(self, window)
		self.language = win.language
		self.frame = tk.LabelFrame(self.window,text=self.language[22],borderwidth=4,relief="groove")

	def checkalogw(self, event):
		if self.attackAlgoW.get() in commands_list:
			self.attackTypeW.config(state="readonly")
			self.lengthkey.config(state="normal")
		else:
			self.attackTypeW.config(state="disabled")
			self.lengthkey.config(state="disabled")

	def attackAlgo(self, commands_list):
		self.Commandtype = tk.Label(self.frame,text=self.language[23])
		self.attackAlgoW = ttk.Combobox(self.frame)
		options = commands_list
		self.attackAlgoW["values"] = options
		self.attackAlgoW.set(self.attackAlgoW["values"][0])
		self.attackAlgoW.bind("<<ComboboxSelected>>", self.checkalogw)

	def attackType(self, types_list):
		self.Attacktype = tk.Label(self.frame,text=self.language[24])
		self.attackTypeW = ttk.Combobox(self.frame)
		options = types_list
		self.attackTypeW["values"] = options
		self.attackTypeW.set(self.attackTypeW["values"][0])

	def hashedKey(self):
		self.Hashtype = tk.Label(self.frame,text=self.language[25])
		self.hashedkey = ttk.Entry(self.frame)
		self.hashedkey.insert(0, self.language[26])

	def __getHash(self):
		return self.hashedkey.get()

	def lengthKey(self):
		self.Ltype = tk.Label(self.frame,text=self.language[27])
		self.lengthkey = ttk.Entry(self.frame)
		self.lengthkey.insert(0, self.language[28])

	def __getOption(self):
		option = self.attackAlgoW.get()
		for o in zip(commands_list, char_options):
			if o[0] == option:
				return o[1]
			else:
				continue

	def __start_btn_cmd(self, S):
		if not Start.STOPPSWD:
			result = messagebox.showwarning(self.language[31], self.language[32])
		else:
			Start.STOPPSWD = False
			self.task = threading.Thread(target=S.attackHash, args=(
				self.attackTypeW.get(), self.__getHash(), self.lengthkey.get(), 
				self.__getOption()))
			self.task.start()

	def __stop_btn_cmd(self):
		Start.STOPPSWD = True

	def start_btn(self, S):
		self.stabtn = tk.Button(self.frame,text=self.language[29],
				command=lambda :self.__start_btn_cmd(S))

	def stop_btn(self):
		self.stobtn = tk.Button(self.frame,text=self.language[30],
			command=self.__stop_btn_cmd)

	def pack(self):
		#-------------------------------------
		self.Commandtype.grid(row=0, column=0, sticky="w")
		self.attackAlgoW.grid(row=0, column=1, sticky="w")
		#-------------------------------------
		self.Attacktype.grid(row=1, column=0, sticky="w")
		self.attackTypeW.grid(row=1, column=1, sticky="w")
		#-------------------------------------
		self.Hashtype.grid(row=2, column=0, sticky="w")
		self.hashedkey.grid(row=2, column=1, sticky="w")
		#-------------------------------------
		self.Ltype.grid(row=3, column=0, sticky="w")
		self.lengthkey.grid(row=3, column=1, sticky="w")
		#-------------------------------------
		self.stabtn.grid(row=4, column=0, columnspan=2, sticky="ew")
		self.stobtn.grid(row=5, column=0, columnspan=2, sticky="ew")
