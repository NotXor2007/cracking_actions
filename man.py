from const import*

class Manual:
	
	def __init__(self,title, commands_list, available_types):
		print("cracking actions v0.7 manual")
		print("------------Usage------------")
		print("universal commands:")
		print("++++exit or quit ==> exit++++")
		print("++++help ==> for help++++")
		print("++++clear ==> clear the console++++")
		print("++++gcp ==> get current page++++")
		print("main commands:")
		print("++++pswdattack ==> switch password cracker page(hash only!)++++")
		print("++++zipattack ==> switch to zip cracker page++++")
		print("pswdattack commands:")
		print("++++zipattack ==> switch to zip cracker page++++")
		print("++++main ==> switch to main page++++")
		print("password attacker:") 
		print("++++commands++++")
		for _ in commands_list_man:
			print("++++-----"+_+"-----++++")
		print("++++Algorithms++++")
		for _ in available_types:
			print("++++-----"+_+"-----++++")
		print("++++Hash++++")
		print("++++----provide a key to decrypt----++++")
		print("++++Mgl++++")
		print("++++----maximum generated length----++++")
		print("zipattack commands:")
		print("++++pswdattack ==> switch password cracker page(hash only!)++++")
		print("++++main ==> switch to main page++++")
		print("zip attacker:") 
		print("++++commands++++")
		for _ in commands_list_man:
			print("++++-----"+_+"-----++++")
		print("++++Mgl++++")
		print("++++----maximum generated length----++++")
		print("++++path++++")
		print("++++----provide path to the zip file----++++")
		print("++++output++++")
		print("++++----provide path to the extracted data----++++")
