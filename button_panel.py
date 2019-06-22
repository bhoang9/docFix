from tkinter import *
from button_functions import *

class button_panel:

	def __init__(self, root, frame, before_text_box, after_text_box):
		self.root = root
		self.frame = frame

		test_button = None
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

		self.test_button = Button(self.root, text="exit")
		self.insertBottomButton = Button(self.root, text="insertBottomButton")
		self.specialCharButton = Button(self.root, text="specialCharButton")
		self.fixSpecialButton = Button(self.root, text="Fix debug")

	def define_buttons(self):
		self.test_button.configure(command = lambda : client_exit())
		
		self.insertBottomButton.configure(command = 
			lambda: insert_tBox(self.afterTextBox, self.beforeTextBox.get("1.0", END)))

		self.specialCharButton.configure(command = 
			lambda: get_ascii(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

		self.fixSpecialButton.configure(command =
			lambda: fix_special(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

	def place_buttons(self):
		self.test_button.place(x=10, y=10)
		self.insertBottomButton.place(x=10, y=40)
		self.specialCharButton.place(x=10,y=70)
		self.options.place(x=10,y=100)
		self.fixSpecialButton.place(x=10, y=130)

	def init_options_menu(self):
		string_var = StringVar(self.frame)
		string_var.set("Add HTML tags")

		option_choices = ["Bold", "Italic", "Underline", "Bold Underline", "Bold Italic",
					"All"]

		options = OptionMenu(self.root, string_var, *option_choices,
			command = lambda x: add_html_tag(self.afterTextBox, self.beforeTextBox.get("1.0", 'end-1c'), string_var.get()))

		self.options = options

