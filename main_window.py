#Version to deploy

#Eventually want to compartamentalize button definitions and have layout of
#elemnts(buttons, text entry, etc) properly defined

from tkinter import *
from button_functions import *
from button_panel import *
from textbox_panel import *
import unicodedata

class Window(Frame):

	def __init__(self, master=None):

		self.root = Tk() #make the window
		self.root.config(background = "grey")
		#Frame.__init__(self,master)
		self.root.wm_title("Doc Fixer")
		self.root.geometry("800x600")
		self.root.config(background = "#808080")
		self.master = master

		self.init_main_window()

		self.button_panel = Frame(self.root, width=200, height = 550)
		self.button_panel.grid(row=0, column=0, padx=5, pady=5)

		self.textbox_panel = Frame(self.root, width=600, height = 600)
		self.textbox_panel.grid(row=0, column=1, padx=5, pady=5)

		self.textbox_panel = textbox_panel(self.root, self.textbox_panel)
		self.button_panel = button_panel(self.root, self.button_panel, 
			self.textbox_panel.get_before_textbox(), self.textbox_panel.get_after_textbox())


		#old implementation of main window where everything is essentially run
		#in main()

		#self.init_window()

	def init_main_window(self):
		menu = Menu(self.root)
		file = Menu(menu)
		edit = Menu(menu)
		file.add_command(label="Exit", command=client_exit)

		self.root.config(menu=menu)

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
			command = lambda: insert_tBox(afterTextBox, beforeTextBox.get("1.0", 'end-1c')))

		insertTopButton = Button(self, text="Bottom to Top",
			command = lambda: insert_tBox(beforeTextBox, afterTextBox.get("1.0", 'end-1c')))

		deleteButton = Button(self, text="Clear Top", 
			command = lambda: clear_tBox(beforeTextBox))

		bulletsButton = Button(self, text="Fix bullets", 
			command = lambda: fix_bullets(afterTextBox,beforeTextBox.get("1.0", 'end-1c')))

		fixSpecial = Button(self, text="Fix Special Char",
			command = lambda: convert_special(afterTextBox,beforeTextBox.get("1.0", 'end-1c')))

		asciiButton = Button(self, text="Get ASCII",
			command = lambda: get_ascii(afterTextBox,beforeTextBox.get("1.0", 'end-1c')))

		newlineButton = Button(self, text="Fix newline",
			command = lambda: fix_newline(afterTextBox,beforeTextBox.get("1.0", 'end-1c')))

		createListButton = Button(self, text="Create list",
			command = lambda: create_list(afterTextBox,beforeTextBox.get("1.0", 'end-1c')))

		exitButton = Button(self, text="Exit",
			command = lambda: client_exit())

		#getting option menu
		options = self.init_options_menu(afterTextBox, beforeTextBox)


		#self.master.title("Doc Fixer")
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
		newlineButton.place(x=10, y=160)
		options.place(x=10, y=190)
		createListButton.place(x=10, y=220)
		asciiButton.place(x=10, y=250)
		exitButton.place(x=10, y=280)

	def start(self):
		self.root.mainloop()

	def getAfterbox(self):
		return self.afterTextBox.get("1.0", 'end-1c')

	def getBeforeTextbox(self):
		return self.beforeTextBox.get("1.0", 'end-1c')

	def init_options_menu(self, aftTextBox, befTextBox):
		string_var = StringVar(self.root)
		string_var.set("Add HTML tags")

		option_choices = ["Bold", "Italic", "Underline", "Bold Underline", "Bold Italic",
					"All"]

		options = OptionMenu(self.master, string_var, *option_choices,
			command = lambda x: add_html_tag(aftTextBox, befTextBox.get("1.0", 'end-1c'), string_var.get()))

		return options
