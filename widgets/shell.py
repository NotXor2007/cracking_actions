from const import*
import tkinter as tk

class Shell:

	def __init__(self, win):
		self.win = win
		self.shell = self.win.out.console
		self.waitfcmd(None)
		self.shell.bind("<Return>", self.waitfcmd)

	def waitfcmd(self, event):
		cpos = self.shell.index(tk.INSERT)
		self.shell.insert("end", "\n==> ")
