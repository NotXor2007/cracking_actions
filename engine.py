import os
import hashlib
import zipfile, rarfile
from const import*
from itertools import product
from colorama import Fore

#start contains cracking alghoritms
class Start:
	STOPPSWD, STOPZIP, STOPRAR = True, True, True
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

	def attackHash(self, hash_type, hashed_key, length_key, option, cli=False):
		if option == None and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong command")
			return
		if hash_type not in available_types and cli:
			Start.STOPPSWD = True
			print(Fore.WHITE + "Warning:wrong Algorithm")
			return
		if len(hashed_key.strip()) == 0:
			if not cli:
				self.win.out.pswdout.insert("end","Warning:wrong hash key\n")
			else:
				print(Fore.WHITE + "Warning:wrong hash key")
			Start.STOPPSWD = True
			return False
		elif not length_key.strip().isnumeric():
			if not cli:
				self.win.out.pswdout.insert("end","Warning:Mgl must be a number!\n")
			else:
				print(Fore.WHITE + "Warning:Mgl must be a number!")
			Start.STOPPSWD = True
			return False
		length_key = int(length_key.strip())
		for length in range(length_key+1):
			for keys in product(option,repeat = length):
				if Start.STOPPSWD:
					return
				key = "".join(keys)
				new_key = key.encode()
				self.result = self.show_check(hash_type,new_key,hashed_key,key)
				self.__printHash(self.result[0],key,self.result[1],hashed_key,cli)
				if not cli:
					self.win.readraw()
					self.win.Aupdate()
				if self.result[0] == 1:
					Start.STOPPSWD = True
					return
				else:
					continue
		if not cli:
			self.win.out.pswdout.insert("end","key not found!\n")
		else:
			print(Fore.WHITE + "key not found!")
		Start.STOPPSWD = True

	def attackZip(self, file, output, length_key, option, cli=False):
		result = 0
		if option == None and cli:
			Start.STOPZIP = True
			print("Warning:wrong command")
			return
		elif not length_key.strip().isnumeric():
			if not cli:
				self.win.out.zipout.insert("end","Warning:Mgl must be a number!\n")
			else:
				print("Warning:Mgl must be a number!")
			Start.STOPZIP = True
			return False
		length_key = int(length_key.strip())
		for length in range(length_key+1):
			for keys in product(option,repeat = length):
				if Start.STOPZIP:
					return
				key = "".join(keys)
				try:
					f = zipfile.ZipFile(file)
					self.__printcompressed(self.win.out.zipout, key, file, cli)
					try:
						f.setpassword(pwd=key.encode())
						f.extractall(output)
						f.close()
						if not cli:
							self.win.out.zipout.insert("end",f"key found:{key}\n")
						else:
							print(f"key found:{key}")
						result = 1
					except RuntimeError as e:
						continue
				except Exception as e:
					if not cli:
						self.win.out.zipout.insert("end","Warning:incorrect file name or path!\n")
					else:
						print("Warning:incorrect file name or path!")
					continue #this is crucial
				#exit if key was found
				if result == 1:
					Start.STOPZIP = True
					return
				else:
					continue
				if not cli:
					self.win.out.zipout.insert("end","current key is "+key)
					self.win.readraw()
					self.win.Aupdate()
				else:
					print("current key is "+key)
		if not cli:
			self.win.out.zipout.insert("end","key not found!\n")
		else:
			print("key not found!")
		Start.STOPZIP = True

	def attackRar(self, file, output, length_key, option, cli=False):
		result = 0
		if option == None and cli:
			Start.STOPRAR = True
			print("Warning:wrong command")
			return
		elif not length_key.strip().isnumeric():
			if not cli:
				self.win.out.zipout.insert("end","Warning:Mgl must be a number!\n")
			else:
				print("Warning:Mgl must be a number!")
			Start.STOPRAR = True
			return False
		length_key = int(length_key.strip())
		for length in range(length_key+1):
			for keys in product(option,repeat = length):
				if Start.STOPRAR:
					return
				key = "".join(keys)
				try:
					f = rarfile.RarFile(file)
					self.__printcompressed(self.win.out.rarout, key, file, cli)
					try:
						f.setpassword(pwd=key.encode())
						f.extractall(output)
						f.close()
						if not cli:
							self.win.out.rarout.insert("end",f"key found:{key}\n")
						else:
							print(f"key found:{key}")
						result = 1
					except RuntimeError as e:
						continue
				except Exception as e:
					if not cli:
						self.win.out.rarout.insert("end","Warning:incorrect file name or path!\n")
					else:
						print("Warning:incorrect file name or path!")
					continue #this is crucial
				#exit if key was found
				if result == 1:
					Start.STOPRAR = True
					return
				else:
					continue
				if not cli:
					self.win.out.rarout.insert("end","current key is "+key)
					self.win.readraw()
					self.win.Aupdate()
				else:
					print("current key is "+key)
		if not cli:
			self.win.out.rarout.insert("end","key not found!\n")
		else:
			print("key not found!")
		Start.STOPRAR = True
