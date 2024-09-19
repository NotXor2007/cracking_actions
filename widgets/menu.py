import tkinter as tk

class MenuBar:

	def __init__(self, win, window, on_closing, get_help, pswdatk, zipatk, raratk, load_wlst, settings, mwin):
		self.menu_bar = tk.Menu(window)
		self.on_closing = on_closing
		self.get_help = get_help
		self.pswdatk = pswdatk
		self.zipatk = zipatk
		self.raratk = raratk
		self.settings = settings
		self.load_wlst = load_wlst
		self.mwin = mwin
		self.language = win.language
		self.__exit()
		self.__help()
		self.__about()
		window.configure(menu = self.menu_bar)
		self.pswdatk_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.zipatk_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.raratk_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.settings_menu = tk.Menu(self.menu_bar, tearoff=False)
		self.menu_bar.add_cascade(label=self.language[4], 
			menu=self.pswdatk_menu)
		self.__attack_pswd_e()
		self.__attak_zip_e()
		self.__attak_rar_e()
		self.__load_wlist_e()
		self.__settings_e()
	#creating menus and calling events
	def __exit(self):
		self.menu_bar.add_command(label=self.language[1], command = self.on_closing)

	def __help(self):
		self.menu_bar.add_command(label=self.language[2], command = self.get_help)

	def __about(self):
		self.menu_bar.add_command(label=self.language[3], command = self.mwin)

	def __attack_pswd_e(self):
		self.pswdatk_menu.add_command(label=self.language[5], 
			command = self.pswdatk)

	def __attak_zip_e(self):
		self.pswdatk_menu.add_command(label=self.language[6], 
			command = self.zipatk)

	def __attak_rar_e(self):
		self.pswdatk_menu.add_command(label=self.language[7], 
			command = self.raratk)

	def __load_wlist_e(self):
		self.pswdatk_menu.add_command(label="load wordlist", 
			command = self.load_wlst)

	def __settings_e(self):
		self.menu_bar.add_command(label=self.language[8], 
			command = self.raratk)
