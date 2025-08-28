import tkinter as tk
from tkinter import ttk
from win32ui import MessageBox
from win32con import*
from tkinter import filedialog

class Writer:
    def __init__(self): pass

    def __encode(self, data, option):
            ret_str = str()
            for char in data:
                    for index in range(0, len(option), 1):
                            if option[index] == char: ret_str += (str(index) + " ")
            return ret_str[:len(ret_str)-1]

    #load progress file
    def __save_file(self, data, option):
        file = filedialog.asksaveasfile(title="Save Progress File As",
                                        filetypes=[("CAPS file", ".caps")],defaultextension=".caps")
        if file != None:
            file.write(self.__encode(data, option))
            file.close()

    #load progress
    def write(self, data, option):
        if MessageBox("Do you want to save the cracking session?", "cracking-actions 0.9 alpha", MB_YESNO | MB_ICONQUESTION) == 6:
            return self.__save_file(data, option)
        return [-1, ]

class Loader:

    def __init__(self): self.loop = True
    
    #show load window for linux version
    def __show_load_dialog(self, window):
        dialog = tk.Toplevel(window)
        dialog.protocol("WM_DELETE_WINDOW", self.__exit)
        while self.loop:
            dialog.update()
            dialog.update_idletasks()
        dialog.destroy()

    #read file data
    def __readcaps(self, file):
        data_lst = file.readline().split(" ")
        for index in range(0, len(data_lst), 1):
                data_lst[index] = int(data_lst[index])
        file.close()
        return data_lst

    #load progress file
    def __load_file(self, window):
        file = filedialog.askopenfile(parent = window, title="Open Progress File", filetypes=[("CAPS file", "*.caps")])
        if file != None: return self.__readcaps(file)
        return [-1, ]

    #load progress
    def load(self, window):
        if MessageBox("Do you want to load a previous cracking session?", "cracking-actions 0.9 alpha", MB_YESNO | MB_ICONQUESTION) == 6:
            return self.__load_file(window)
        return [-1, ]
