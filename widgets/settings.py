import tkinter as tk
from tkinter import ttk
from const import*

class Settings:

	def __init__(self, win):
		self.win = win
		self.settings_window = None
		self.language_selector = None
		self.language_frame = None
		self.apply_frame = None
		self.apply = None

	def show_settings(self):
		self.__window()
		self.__frames()
		self.__widgets()
		self.__pack()

	def __window(self):
		self.settings_window = tk.Toplevel(self.win.window)
		self.settings_window.wm_attributes("-topmost", True)
		self.settings_window.wm_attributes("-alpha", 1)
		self.settings_window.resizable(False, False)
		self.settings_window.geometry("600x400")
		self.settings_window.iconbitmap(icon)
		self.settings_window.title("cracking actions v0.8-Settings")

	def __frames(self):
		self.language_frame = tk.LabelFrame(self.settings_window,text="select language",borderwidth=4,relief=tk.FLAT)
		self.apply_frame = tk.LabelFrame(self.settings_window,text="apply changes",borderwidth=4,relief=tk.FLAT)

	def __language(self):
		self.language_selector = ttk.Combobox(self.language_frame)
		self.language_selector["values"] = language_list
		self.language_selector.set(self.language_selector["values"][0])

	def __apply(self):
		self.apply = tk.Button(self.apply_frame, text = "Apply", command = None)

	def __widgets(self):
		self.__language()
		self.__apply()
	
	def __pack(self):
		self.language_frame.pack()
		self.language_selector.pack()
		self.apply_frame.pack()
		self.apply.pack()
	