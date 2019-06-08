from tkinter import *

def showText(self):
	text = Label(self, text="Greetings")
	text.pack()

def client_exit():
	sys.exit()

def print_entry(self, newString):
		print(newString)

	#Insert text into a textBox
def insert_tBox(tBox, nString):
	clear_tBox(tBox)
	tBox.insert(END, nString)

#clear the input box
def clear_tBox(tBox):
	tBox.delete('1.0', END)

#Format bulletpoints correctly
def fix_bullets(tBox, nString):
	writeStr = "<ul>"

	for c in nString:
		if (ord(c) == 8226) or (ord(c) == 9679):
			writeStr += "<li>"

		elif(ord(c) == 10):
			writeStr += "</li>"

		else:
			writeStr += c
	writeStr +="</li></ul>"
	clear_tBox(tBox)
	tBox.insert(END, writeStr)

	#Create an HTML list w/ lines separated by "\n"
def create_list(tBox, nString):
	writeStr = "<ul><li>"
	for c in nString:

		if(ord(c) == 10):
			writeStr += "</li><li>"

		else:
			writeStr += c

	writeStr += "</li></ul>"
	clear_tBox(tBox)
	tBox.insert(END, writeStr)

			#convert Spanish and unicode punctuation into their HTML and ASCII 
	#equivalent
def convert_special(tBox, nString):
	writeStr = ""
	specialCharDict = {193:"&#193;", 201:"&#201;", 205:"&#205;", 211:"&#211;", 
				218:"&#218;",209: "&#209;", 220: "&#220;", 225: "&#225;", 
				233: "&#233;",237:"&#237;", 243: "&#243;",250:"&#250;", 
				241: "&#241;", 252: "&#252;", 191: "&#191;", 161: "&#161;",
				8220: '"', 8221: '"', 8217: "'"}
	newline = False

#Some Spanish characters are interpreted as a regular letter with the
#accent mark added to them; ex: 'Small latin "o" with acute'
#These are read as a string b/c the letter and the accompanying
#accent mark are read separately, but are printed seemingly together

#					{ 65 769: "&#193;", 69 769:"&#201;",
#					73 769:"&#205;", 79 769:"&#211;", 85 769:"&#218;", 78 771: "&#209;", 
#					85 776: "&#220;", 97 769: "&#225;", 101 769: "&#233;", 105 769:"&#237;", 
#					111 769: "&#243;", 117 769:"&#250;", 110 771: "&#241;", 117 776: "&#252;"}

		#check if Char exists in dictionary of special characters
	for c in nString:

#		if(ord(c) in specialCharDict):
#			writeStr += specialCharDict[ord(c)]
#		else:
#			writeStr += c

		writeStr += specialCharDict.get(ord(c), c)

	clear_tBox(tBox)
	tBox.insert(END, writeStr)

def get_ascii(tBox, nString):
	writeStr = ""
	for c in nString:
		if(ord(c) == 32):
			writeStr += " "

		elif(ord(c) == 10):
			writeStr += c

		else:	
			writeStr += str(ord(c))

	clear_tBox(tBox)
	tBox.insert(END, writeStr)

	#fix newlines caused by formatting software
def fix_newline(tBox, nString):

	writeStr = ""
	newline = False
	for c in nString:

		#if(ord(c) == 10):
		#	writeStr += " "

		if(ord(c) == 10) and (newline == False):
			newline = True

		else:
			newline = False
			writeStr += c


	clear_tBox(tBox)
	tBox.insert(END, writeStr)