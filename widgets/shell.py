from const import*

class Shell:

	def __init__(self, win):
		self.win = win
		self.shell = self.win.out.console
		self.waitfcmd()

	def waitfcmd(self):
		self.shell.insert("end", "==> ")
