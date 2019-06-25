from tkinter import *
import button_dictionaries

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
def create_list(tBox, nString, newline):

	writeStr = "<ul>"
	newList = nString.splitlines()

	if(newline == True):
		closingTag = "\n</li>"
	else:
		closingTag = "</li>"

	for item in newList:
		nItem = "<li>" + item + closingTag
		writeStr += nItem

	writeStr += "</ul>"

	clear_tBox(tBox)
	tBox.insert(END, writeStr)

#convert Spanish and unicode punctuation into their HTML and ASCII 
#equivalent
def convert_special(tBox, nString):
	writeStr = ""

	#dictionary of special character keys assigned to their HTML/plaintext values
	specialCharDict = button_dictionaries.specialCharDict

	#check if Char exists in dictionary of special characters
	for c in nString:

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

	#Feel like there are some redundancies in here somewhere
	#Will refine later
	for c in nString:

		if(ord(c) == 10):
			if(newline == False):
				writeStr += " "
				newline = True
			else:
				writeStr += "\n"
		else:
			newline = False
			writeStr += c

	clear_tBox(tBox)
	tBox.insert(END, writeStr)

#Add html tags around a string
def add_html_tag(tBox, nString, html_tag):

	openingTag = button_dictionaries.html_tags[html_tag][0]
	closingTag = button_dictionaries.html_tags[html_tag][1]
	tagged_string = openingTag + nString + closingTag

	clear_tBox(tBox)
	tBox.insert(END, tagged_string)

def fix_special(tBox, nString):
	writeStr = ""
	newline = False

	for c in nString:

		if(ord(c) == 10):
			writeStr += " "

		else:
			writeStr += c

	clear_tBox(tBox)
	tBox.insert(END, writeStr)

#for testing purposes
def print_string(tBox, nString):

	clear_tBox(tBox)
	tBox.insert(nString)