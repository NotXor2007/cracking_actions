import tkinter as tk
from tkinter import ttk
from supercls import Widgets

class OutputTerm(Widgets):

	def __init__(self, window):
		Widgets.__init__(self, window)
		self.frame = tk.LabelFrame(self.window,borderwidth=4,text="output",relief="groove")
		self.notebook = ttk.Notebook(self.frame)
		self.pswdtab = ttk.Frame(self.notebook)
		self.ziptab = ttk.Frame(self.notebook)
		self.rartab = ttk.Frame(self.notebook)
		self.console = ttk.Frame(self.notebook)
		self.notebook.add(self.pswdtab, text="password attacker output")
		self.notebook.add(self.ziptab, text="zip attacker output")
		self.notebook.add(self.rartab, text="rar attacker output")
		self.notebook.add(self.console, text="shell")

	def output(self):
		self.pswdout = tk.Text(self.pswdtab)
		self.zipout = tk.Text(self.ziptab)
		self.rarout = tk.Text(self.rartab)
		self.console = tk.Text(self.console)

	def pack(self):
		self.notebook.pack()
		self.pswdout.grid(row=0, column=0, sticky="n")
		self.zipout.grid(row=0, column=0, sticky="n")
		self.rarout.grid(row=0, column=0, sticky="n")
		self.console.grid(row=0, column=0, sticky="n")
