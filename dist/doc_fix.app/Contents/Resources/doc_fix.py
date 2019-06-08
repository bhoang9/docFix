#Version to deploy

from tkinter import *
from buttonFunctions import *
import unicodedata

class Window(Frame):
	def __init__(self, master=None):

		Frame.__init__(self,master)

		self.master = master

		self.init_window()

	def init_window(self):
		menu = Menu(self.master)
		file = Menu(menu)
		edit = Menu(menu)
		entry = Entry(self)

		#textbox showing text before, and the text after modifications
		beforeTextBox = Text(self, height=18,width=80, borderwidth=2, relief="solid")
		afterTextBox = Text(self, height=18, width=80, borderwidth=2, relief="solid")

		#buttons
		showButton = Button(self, text="Show", command = lambda: self.print_entry(entry.get()))

		insertBottomButton = Button(self, text="Top to Bottom", 
			command = lambda: insert_tBox(afterTextBox, beforeTextBox.get("1.0", END)))

		insertTopButton = Button(self, text="Bottom to Top",
			command = lambda: insert_tBox(beforeTextBox, afterTextBox.get("1.0", END)))

		deleteButton = Button(self, text="Clear Top", 
			command = lambda: clear_tBox(beforeTextBox))

		bulletsButton = Button(self, text="Fix bullets", 
			command = lambda: fix_bullets(afterTextBox,beforeTextBox.get("1.0", END)))

		fixSpecial = Button(self, text="Fix Special Char",
			command = lambda: convert_special(afterTextBox,beforeTextBox.get("1.0", END)))

		asciiButton = Button(self, text="Get ASCII",
			command = lambda: get_ascii(afterTextBox,beforeTextBox.get("1.0", END)))

		newlineButton = Button(self, text="Fix newline",
			command = lambda: fix_newline(afterTextBox,beforeTextBox.get("1.0", END)))

		createListButton = Button(self, text="Create list",
			command = lambda: create_list(afterTextBox,beforeTextBox.get("1.0", END)))

		exitButton = Button(self, text="Exit",
			command = lambda: client_exit())


		self.master.title("Doc Fixer")
		self.pack(fill=BOTH, expand=1)
		self.master.config(menu=menu)

		#beforeTextBox.pack(side = TOP, fill = BOTH, expand = True)
		#afterTextBox.pack(side = BOTTOM, fill = BOTH, expand = True)

		file.add_command(label="Exit", command=self.client_exit)
		menu.add_cascade(label="File", menu=file)

		beforeTextBox.place(x=150,y=10)
		afterTextBox.place(x=150,y=300)

		#placing buttons
		insertBottomButton.place(x=10,y=10)
		insertTopButton.place(x=10,y=40)
		deleteButton.place(x=10,y=70)
		bulletsButton.place(x=10,y=100)
		fixSpecial.place(x=10, y=130)
		asciiButton.place(x=10, y=160)
		newlineButton.place(x=10, y=190)
		createListButton.place(x=10, y=230)
		exitButton.place(x=10, y=260)

	def showText(self):
		text = Label(self, text="Greetings")
		text.pack()

	def client_exit(self):
		sys.exit()

	def print_entry(self, newString):
		print(newString)

	#Insert text into a textBox
	def insert_tBox(self, tBox, nString):
		self.clear_tBox(tBox)
		tBox.insert(END, nString)

	#clear the input box
	def clear_tBox(self, tBox):
		tBox.delete('1.0', END)

	#Format bulletpoints correctly
	def fix_bullets(self, tBox, nString):
		writeStr = "<ul>"

		for c in nString:
			if (ord(c) == 8226) or (ord(c) == 9679):
				writeStr += "<li>"

			elif(ord(c) == 10):
				writeStr += "</li>"

			else:
				writeStr += c

		writeStr +="</li></ul>"

		self.clear_tBox(tBox)
		tBox.insert(END, writeStr)

	#Create an HTML list w/ lines separated by "\n"
	def create_list(self, tBox, nString):
		writeStr = "<ul><li>"

		for c in nString:
			if(ord(c) == 10):
				writeStr += "</li><li>"

			else:
				writeStr += c

		writeStr += "</li></ul>"

		self.clear_tBox(tBox)
		tBox.insert(END, writeStr)

	#convert Spanish and unicode punctuation into their HTML and ASCII 
	#equivalent
	def convert_special(self, tBox, nString):
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

#			if(ord(c) in specialCharDict):
#				writeStr += specialCharDict[ord(c)]
#			else:
#				writeStr += c

			writeStr += specialCharDict.get(ord(c), c)

		self.clear_tBox(tBox)
		tBox.insert(END, writeStr)

	def get_ascii(self, tBox, nString):

		writeStr = ""

		for c in nString:
			if(ord(c) == 32):
				writeStr += " "

			elif(ord(c) == 10):
				writeStr += c

			else:	
				writeStr += str(ord(c))

		self.clear_tBox(tBox)
		tBox.insert(END, writeStr)

	#fix newlines caused by formatting software
	def fix_newline(self, tBox, nString):

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


		self.clear_tBox(tBox)
		tBox.insert(END, writeStr)

root = Tk()
root.geometry("800x600")
app = Window(root)
root.configure(background="grey")
root.mainloop()