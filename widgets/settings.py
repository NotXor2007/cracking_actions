import tkinter as tk
from tkinter import ttk
from const import*
from core import cfghandler
from supercls import Widgets
from tkinter import colorchooser

class Settings(Widgets):

	def __init__(self, win, window, language):
		Widgets.__init__(self, window)
		self.win = win
		self.settings_window = None
		self.language_selector = None
		self.language_frame = None
		self.apply_frame = None
		self.apply = None
		self.language = language

	def show_settings(self):
		self.__window()
		self.__frames()
		self.__widgets()
		self.__pack()

	def __window(self):
		self.settings_window = tk.Toplevel(self.win.window)
		self.settings_window.wm_attributes("-topmost", True)
		self.settings_window.wm_attributes("-alpha", 1)
		#self.settings_window.resizable(False, False)
		self.settings_window.geometry("600x400")
		self.settings_window.iconbitmap(icon)
		self.settings_window.title(self.win.language[14])

	def __frames(self):
		self.language_frame = tk.LabelFrame(self.settings_window,text=self.win.language[15],borderwidth=4,relief=tk.FLAT)
		self.apply_frame = tk.LabelFrame(self.settings_window,text=self.win.language[19],borderwidth=4,relief=tk.FLAT)

	def __language(self):
		self.language_selector = ttk.Combobox(self.language_frame)
		self.language_selector["values"] = (self.win.language[16], self.win.language[17], self.win.language[18])
		self.language_selector.set(self.language[0])

	def __get_selection(self):
		return self.language_selector.get()

	def __apply(self):
		if self.__get_selection() == self.win.language[16]:
			cfghandler.writecfg(["LANGUAGE=.\lang\english.lang"])
		elif self.__get_selection() == self.win.language[17]:
			cfghandler.writecfg(["LANGUAGE=.\lang\\french.lang"])
		elif self.__get_selection() == self.win.language[18]:
			cfghandler.writecfg(["LANGUAGE=.\lang\\arabic.lang"])

	def __applybtn(self):
		self.apply = tk.Button(self.apply_frame, text = self.win.language[20], command = self.__apply)

	def __widgets(self):
		self.__language()
		self.__applybtn()
	
	def __pack(self):
		tk.Grid.columnconfigure(self.settings_window, 0, weight=1)
		tk.Grid.columnconfigure(self.settings_window, 1, weight=1)
		self.language_frame.grid(row=0, column=0, sticky = "nw")
		self.language_selector.pack()
		self.apply_frame.grid(row=1, column=1, sticky = "se")
		self.apply.pack()
	