from tkinter import *
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
		beforeTextBox = Text(self, height=10,width=80, borderwidth=2, relief="solid")
		afterTextBox = Text(self, height=10, width=80, borderwidth=2, relief="solid")

		#buttons
		showButton = Button(self, text="Show", command = lambda: self.print_entry(entry.get()))

		insertButton = Button(self, text="insert", 
			command = lambda: self.insert_tBox(afterTextBox, beforeTextBox.get("1.0", END)))

		deleteButton = Button(self, text="Clear", command = lambda: self.clear_tBox(beforeTextBox))

		bulletsButton = Button(self, text="Fix bullets", 
			command = lambda: self.fix_bullets(afterTextBox,beforeTextBox.get("1.0", END)))

		fixEspButton = Button(self, text="Convert Spanish",
			command = lambda: self.convert_esp(afterTextBox,beforeTextBox.get("1.0", END)))

		asciiButton = Button(self, text="Get ascii",
			command = lambda: self.get_ascii(afterTextBox,beforeTextBox.get("1.0", END)))


		self.master.title("GUI")
		self.pack(fill=BOTH, expand=1)
		self.master.config(menu=menu)

		beforeTextBox.pack()
		afterTextBox.pack()

		file.add_command(label="Exit", command=self.client_exit)
		edit.add_command(label="Show Text", command=self.showText)

		menu.add_cascade(label="File", menu=file)
		menu.add_cascade(label = "Edit", menu=edit)

		#placing buttons
		insertButton.place(x=10,y=10)
		deleteButton.place(x=10,y=40)
		bulletsButton.place(x=10,y=70)
		fixEspButton.place(x=10, y=100)
		asciiButton.place(x=10, y=130)

	def showText(self):
		text = Label(self, text="Greetings")
		text.pack()

	def client_exit(self):
		exit()

	def print_entry(self, newString):
		print(newString)

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

	#convert Spanish characters into their HTML equivalent
	def convert_esp(self, tBox, nString):
		writeStr = ""

		specialCharDict = {193:"&#193;", 201:"&#201;", 205:"&#205;", 211:"&#211;", 
					218:"&#218;",209: "&#209;", 220: "&#220;", 225: "&#225;", 
					233: "&#233;",237:"&#237;", 243: "&#243;",250:"&#250;", 
					241: "&#241;", 252: "&#252;", 191: "&#191;", 161: "&#161;"}

		for c in nString:
			if(ord(c) in specialCharDict):
				writeStr += specialCharDict[ord(c)]
			else:
				writeStr += c

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

root = Tk()

root.geometry("800x600")

app = Window(root)

root.mainloop()