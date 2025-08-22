import tkinter as tk
from tkinter import ttk
from win32ui import MessageBox
from win32con import*
from tkinter import filedialog

def writecaps(data: list):
	try:
		with open("settings.cfg", "w", encoding = "utf-8") as settings:
			settings.writelines(data)
	except Exception as e:
		return -1

class Loader:

    def __init__(self):
        self.loop = True

    def __exit(self): self.loop = False
    
    #show load window
    def __show_load_dialog(self, window):
        dialog = tk.Toplevel(window)
        dialog.protocol("WM_DELETE_WINDOW", self.__exit)
        while self.loop:
            dialog.update()
            dialog.update_idletasks()
        dialog.destroy()

    def __readcaps(self, file_path):
        try:
            with open(file_path, "r", encoding = "utf-8") as caps:
                data_lst = caps.readline().split(" ")
            for index in range(0, len(data_lst), 1):
                data_lst[index] = int(data_lst[index])
            return data_lst
        except Exception as e:
            return -1

    def __load_file(self):
        file_path = filedialog.askopenfilename(title="Open Progress File",
			filetypes=[("CAPS file", ".caps")])
        if file_path != "": return self.__readcaps(file_path)
        return [-1, ]

    #load progress
    def load(self, window):
        if MessageBox("Do you want to load a previous cracking session?", "cracking-actions 0.9 alpha", MB_YESNO | MB_ICONQUESTION) == 6:
            return self.__load_file()
        return [-1, ]
        #self.__show_load_dialog(window)
