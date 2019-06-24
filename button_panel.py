#Contains the Frame that holds the buttons
#The TextBox objects found in textbox_panel are passed to here

from tkinter import *
from button_functions import *

class button_panel:

	def __init__(self, root, frame, before_text_box, after_text_box):
		self.root = root
		self.frame = frame

		exit_button = None
		insertBottomButton = None
		specialCharButton = None
		options = None
		self.beforeTextBox = before_text_box
		self.afterTextBox = after_text_box

		self.create_buttons()
		self.define_buttons()
		self.init_options_menu()
		self.place_buttons()

	def create_buttons(self):

		self.exit_button = Button(self.root, text="exit")
		self.insertBottomButton = Button(self.root, text="Top to bottom")
		self.specialCharButton = Button(self.root, text="Fix special char")
		self.fixDebugButton = Button(self.root, text="Fix debug")
		self.fixBulletsButton = Button(self.root, text="Fix bullets")
		self.fixNewlineButton = Button(self.root,text="Fix newline")
		self.clearTopButton = Button(self.root,text="Clear top")
		self.getAsciiButton = Button(self.root, text="Get ASCII")

	def define_buttons(self):

		self.exit_button.configure(command = lambda : client_exit())
		
		self.insertBottomButton.configure(command = 
			lambda: insert_tBox(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.specialCharButton.configure(command = 
			lambda: convert_special(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.fixDebugButton.configure(command =
			lambda: fix_special(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.fixBulletsButton.configure(command =
			lambda: fix_bullets(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.fixNewlineButton.configure(command =
			lambda: fix_newline(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.clearTopButton.configure(command =
			lambda: clear_tBox(self.beforeTextBox))

		self.getAsciiButton.configure(command =
			lambda: get_ascii(self.afterTextBox, self.beforeTextBox.get("1.0",END)))			

	def place_buttons(self):
		self.insertBottomButton.place(x=10, y=10)
		self.specialCharButton.place(x=10,y=40)
		self.options.place(x=10,y=70)
		self.fixBulletsButton.place(x=10,y=100)
		self.fixNewlineButton.place(x=10,y=130)
		self.clearTopButton.place(x=10,y=160)
		self.fixDebugButton.place(x=10, y=240)
		self.exit_button.place(x=10, y=270)

	def init_options_menu(self):
		string_var = StringVar(self.frame)
		string_var.set("Add HTML tags")

		option_choices = ["Bold", "Italic", "Underline", "Bold Underline", "Bold Italic",
					"All"]

		options = OptionMenu(self.root, string_var, *option_choices,
			command = lambda x: add_html_tag(self.afterTextBox, self.beforeTextBox.get("1.0", 'end-1c'), string_var.get()))

		self.options = options

