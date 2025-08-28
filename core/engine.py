import os,sys
import hashlib
import zipfile, zipfile_deflate64, zipfile_ppmd, rarfile
from core.capshandler import Writer
from const import*
from colorama import Fore

def getcompression_method(file):
	method_dict = {0:"None",8:"Deflate",9:"deflate64",12:"Bzip2",14:"Lzma",98:"Ppmd"}
	try:
		with zipfile.ZipFile(file, "r") as zfile:
			for zip_info in zfile.infolist():
				method = zip_info.compress_type
		return method_dict[method]
	except Exception as e: pass

def iterate(fn, symbols:str, length:int, start:int, load:list=[-1,], data:str='', iterdepth:int=-1):
	iterdepth += 1
	if load[0] != -1 and len(load) == length+iterdepth:
		start = load[iterdepth]
	for symboli in range(start, len(symbols)):
		if length == 1:
			if( fn(data+symbols[symboli]) ): return True
		elif ( iterate(fn, symbols, length-1, start, load, data+symbols[symboli], iterdepth) ): return True
		if load[0] != -1 and len(load) == length+iterdepth: load[iterdepth] = 0
	return False

def gen(fn, symbols, stlength, maxlength, load_lst=[-1,]):
	if stlength >= 1 and load_lst[0] == -1:
		for length in range(stlength,maxlength+1,1): 
			if( iterate(fn, symbols, length, 0, load=load_lst) ): return True
	elif load_lst[0] != -1:
		for length in range(len(load_lst),maxlength+1,1):
			if( iterate(fn, symbols, length, 0, load=load_lst) ): return True
	return False

#start contains cracking alghoritms
class Start:
	STOPPSWD, STOPZIP, STOPRAR = True, True, True
	DATA = ""
	SUCCESS = False
	def __init__(self, win):
		self.win = win

	#show contains informations and check for password
	def show_check(self, hash_type,new_key,hashed_key,key):
		if hash_type == "md5":
			new_hash = hashlib.md5(new_key).hexdigest()
		elif hash_type == "sha1":
			new_hash = hashlib.sha1(new_key).hexdigest()
		elif hash_type == "blake2b":
			new_hash = hashlib.blake2b(new_key).hexdigest()
		elif hash_type == "blake2s":
			new_hash = hashlib.blake2s(new_key).hexdigest()
		elif hash_type == "sha224":
			new_hash = hashlib.sha224(new_key).hexdigest()
		elif hash_type == "sha384":
			new_hash = hashlib.sha384(new_key).hexdigest()
		elif hash_type == "sha256":
			new_hash = hashlib.sha256(new_key).hexdigest()
		elif hash_type == "sha512":
			new_hash = hashlib.sha512(new_key).hexdigest()
		elif hash_type == "sha3_224":
			new_hash = hashlib.sha3_224(new_key).hexdigest()
		elif hash_type == "sha3_384":
			new_hash = hashlib.sha3_348(new_key).hexdigest()
		elif hash_type == "sha3_256":
			new_hash = hashlib.sha3_256(new_key).hexdigest()
		elif hash_type == "sha3_512":
			new_hash = hashlib.sha3_512(new_key).hexdigest()
		if new_hash == hashed_key:
			return 1,new_hash
		else:
			return 0,new_hash

	def __printHash(self,result,key,new_hash,hashed_key, cli):
		if not cli:
			self.win.out.pswdout.delete("1.0", "end")
			if result:
				self.win.out.pswdout.insert("end","cracking process is done!\n")
				self.win.out.pswdout.insert("end",f"the current key is {key}\n")
				self.win.out.pswdout.insert("end",f"the current hash is {new_hash}\n")
				self.win.out.pswdout.insert("end",f"the hash value of the key is {hashed_key}\n")
				self.win.out.pswdout.insert("end",f"key found:{key}\n")
			else:
				self.win.out.pswdout.insert("end","cracking process started!\n")
				self.win.out.pswdout.insert("end",f"the current key is {key}\n")
				self.win.out.pswdout.insert("end",f"the current hash is {new_hash}\n")
				self.win.out.pswdout.insert("end",f"the hash value of the key is {hashed_key}\n")
		else:
			os.system("cls")
			if result:
				print(Fore.RED + "cracking process is done!")
				print(Fore.RED + f"the current key is {key}")
				print(Fore.RED + f"the current hash is {new_hash}")
				print(Fore.RED + f"the hash value of the key is {hashed_key}")
				print(Fore.RED + f"key found:{key}")
			else:
				print(Fore.RED + "cracking process started!")
				print(Fore.RED + f"the current key is {key}")
				print(Fore.RED + f"the current hash is {new_hash}")
				print(Fore.RED + f"the hash value of the key is {hashed_key}")

	def __printcompressed(self, cracker, key, file, cli):
		if not cli:
			cracker.delete("1.0", "end")
			cracker.insert("end","cracker process started!\n")
			cracker.insert("end",f"the file path is {file}\n")
			cracker.insert("end",f"the current key is {key}\n")
		else:
			os.system("cls")
			print("cracking process started!")
			print(f"the file path is {file}")
			print(f"the current key is {key}")

	def checkHash(self, hash_type, hashed_key, cli):
		def test(key):
			if Start.STOPPSWD: Start.DATA = key;return True
			new_key = key.encode()
			self.result = self.show_check(hash_type,new_key,hashed_key,key)
			self.__printHash(self.result[0],key,self.result[1],hashed_key,cli)
			if not cli:
				self.win.redraw()
				self.win.Aupdate()
			if self.result[0] == 1: Start.STOPPSWD = True;Start.SUCCESS = True
			return False
		return test

	def attackHashWlst(self, hash_type, hashed_key, length_key, option, load_lst=[-1,], cli=False):
		#security checks
		if option == None and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong command")
			return
		if hash_type not in available_types and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong Algorithm")
			return
		if len(hashed_key.strip()) == 0:
			if not cli: self.win.out.pswdout.insert("end","Warning:wrong hash key\n")
			else: print(Fore.WHITE + "Warning:wrong hash key")
			Start.STOPPSWD = True
			return False
		#main
		if self.win.wlist != None: #if a wordlist is selected
			for key in self.win.wlist:
				check = self.checkHash(hash_type, hashed_key, cli)(key)
				if check: return
		Start.STOPPSWD = True

	def attackHash(self, hash_type, hashed_key, length_key, option, load_lst=[-1,], cli=False):
		if option == None and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong command")
			return
		if hash_type not in available_types and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong Algorithm")
			return
		if len(hashed_key.strip()) == 0:
			if not cli: self.win.out.pswdout.insert("end","Warning:wrong hash key\n")
			else: print(Fore.WHITE + "Warning:wrong hash key")
			Start.STOPPSWD = True
			return False
		elif not length_key.strip().isnumeric():
			if not cli: self.win.out.pswdout.insert("end","Warning:Mgl must be a number!\n")
			else: print(Fore.WHITE + "Warning:Mgl must be a number!")
			Start.STOPPSWD = True
			return False
		
		length_key = int(length_key.strip())
		if( gen(self.checkHash(hash_type, hashed_key, cli), option, 1, length_key, load_lst = load_lst) ):
			if not Start.SUCCESS: Writer().write(Start.DATA, option) #save progress
			else: Start.SUCCESS = False
		else:
			if not cli: self.win.out.pswdout.insert("end","key not found!\n")
			else: print(Fore.WHITE + "key not found!")
		Start.STOPPSWD = True

	def checkZip(self, file, output, cli):
		def test(key):
			if Start.STOPZIP: Start.DATA = key;return True
			try:
				f = zipfile.ZipFile(file)
				self.__printcompressed(self.win.out.zipout, key, file, cli)
				try:
					f.setpassword(pwd=key.encode())
					f.extractall(output)
					f.close()
					if not cli: self.win.out.zipout.insert("end",f"key found:{key}\n")
					else: print(f"key found:{key}")
					Start.STOPZIP = True;Start.SUCCESS = True
				except RuntimeError as e: return False
			except Exception as e:
				if not cli: self.win.out.zipout.insert("end","Warning:incorrect file name or path!\n")
				else: print("Warning:incorrect file name or path!")
			return False
		return test

	def attackZip(self, file, output, length_key, option, load_lst=[-1,], cli=False):
		if getcompression_method(file) == "Ppmd": pass #TODO
		#security checks
		if option == None and cli:
			Start.STOPZIP = True
			print("Warning:wrong command")
			return False #??????????????
		elif not length_key.strip().isnumeric():
			if not cli: self.win.out.zipout.insert("end","Warning:Mgl must be a number!\n")
			else: print("Warning:Mgl must be a number!")
			Start.STOPZIP = True
			return False #??????????????
		#main
		length_key = int(length_key.strip())
		if( gen(self.checkZip(file, output, cli), option, 1, length_key, load_lst = load_lst) ):
			if not Start.SUCCESS: Writer().write(Start.DATA, option) #save progress
			else: Start.SUCCESS = False
		else:
			if not cli: self.win.out.zipout.insert("end","key not found!\n")
			else: print("key not found!")
		Start.STOPZIP = True

	def attackZipWlst(self, file, output, cli=False):
		if self.win.wlist != None: #if a wordlist is selected
			for key in self.win.wlist:
				check = self.checkZip(file, output, cli)(key)
				if check: return
		Start.STOPZIP = True

	def checkRar(self, file, output, cli):
                def test(key):
                        if Start.STOPRAR: Start.DATA = key;return True
                        try:
                                f = rarfile.RarFile(file)
                                self.__printcompressed(self.win.out.rarout, key, file, cli)
                                try:
                                        f.setpassword(pwd=key.encode())
                                        f.extractall(output)
                                        f.close()
                                        if not cli: self.win.out.rarout.insert("end",f"key found:{key}\n")
                                        else: print(f"key found:{key}")
                                        Start.STOPRAR = True;Start.SUCCESS = True
                                except RuntimeError as e: return False
                        except Exception as e:
                                if not cli: self.win.out.rarout.insert("end","Warning:incorrect file name or path!\n")
                                else: print("Warning:incorrect file name or path!");return
                        return False
                return test

	def attackRarWlst(self, file, output, cli=False):
		if self.win.wlist != None:
			for key in self.win.wlist:
				check = self.checkRar(file, output, cli)(key)
		Start.STOPRAR = True

	def attackRar(self, file, output, length_key, option, load_lst=[-1,], cli=False):
		if option == None and cli:
			Start.STOPRAR = True
			print("Warning:wrong command")
			return False
		elif not length_key.strip().isnumeric():
			if not cli:
				self.win.out.zipout.insert("end","Warning:Mgl must be a number!\n")
			else:
				print("Warning:Mgl must be a number!")
			Start.STOPRAR = True
			return False
		
		length_key = int(length_key.strip())
		if( gen(self.checkRar(file, output, cli), option, 1, length_key, load_lst = load_lst) ):
			if not Start.SUCCESS: Writer().write(Start.DATA, option) #save progress
			else: Start.SUCCESS = False
		else:
                        if not cli: self.win.out.rarout.insert("end","key not found!\n")
                        else: print("key not found!")
		Start.STOPRAR = True
