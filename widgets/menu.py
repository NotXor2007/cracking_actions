import tkinter as tk

class MenuBar:

	def __init__(self, window, on_closing, get_help, pswdatk, zipatk, mwin):
		self.menu_bar = tk.Menu(window)
		self.on_closing = on_closing
		self.get_help = get_help
		self.pswdatk = pswdatk
		self.zipatk = zipatk
		self.mwin = mwin
		self.__exit()
		self.__help()
		self.__about()
		window.configure(menu = self.menu_bar)
		self.pswdatk_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.zipatk_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.menu_bar.add_cascade(label="attackers", 
			menu=self.pswdatk_menu)
		self.__attack_pswd_e()
		self.__attak_zip_e()

	def __exit(self):
		self.menu_bar.add_command(label="exit", command = self.on_closing)

	def __help(self):
		self.menu_bar.add_command(label="help", command = self.get_help)

	def __about(self):
		self.menu_bar.add_command(label="About", command = self.mwin)

	def __attack_pswd_e(self):
		self.pswdatk_menu.add_command(label="enable password attacker", 
			command = self.pswdatk)

	def __attak_zip_e(self):
		self.pswdatk_menu.add_command(label="enable zip attacker", 
			command = self.zipatk)
