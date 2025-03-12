def greet(name, lang):
	if lang == "German":
		print ("Hallo " + name)
	elif lang == "Spanish":
		print("Hola " + name)
	elif lang == "Mandarin":
		print("Ni hao " + name)
	else:
		print("Hi " + name)

def name_input():
	name = input("Enter name:")
	greet(name)
	
def lang_input():
	 lang = input("Enter your language:")
     
     
	

name_input()
lang_input()
greet()



