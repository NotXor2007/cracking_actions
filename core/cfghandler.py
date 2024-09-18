import os
import logging

def readcfg():
	try:
		with open("settings.cfg", "r", encoding = "utf-8") as settings:
			lines = settings.readlines()
		lanuage = None
		for line in lines:
			if line.startswith("LANGUAGE="):
				with open(line[9 : ], "r", encoding = "utf-8") as lang:
					language = lang.readlines()
		return language
	except Exception as e:
		return -1

def writecfg(data: list):
	try:
		with open("settings.cfg", "w", encoding = "utf-8") as settings:
			settings.writelines(data)
	except Exception as e:
		return -1
