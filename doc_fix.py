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

		file.add_command(label="Exit", command=client_exit)
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

	def getAfterbox():
		return afterTextBox.get("1.0", END)

	def getBeforeTextbox():
		return beforeTextBox.get("1.0", END)

root = Tk()
root.geometry("800x600")
app = Window(root)
root.configure(background="grey")
root.mainloop()