from tkinter import *
from button_functions import *

class button_panel:

	def __init__(self, root, frame, before_text_box, after_text_box):
		self.root = root
		self.frame = frame

		test_button = None
		insertBottomButton = None
		specialCharButton = None
		self.beforeTextBox = before_text_box
		self.afterTextBox = after_text_box

		self.create_buttons()
		self.define_buttons()
		self.place_buttons()

	def create_buttons(self):

		self.test_button = Button(self.frame, text="test Button")
		self.insertBottomButton = Button(self.root, text="insertBottomButton")
		self.specialCharButton = Button(self.root, text="specialCharButton")

	def define_buttons(self):
		self.test_button.configure(command = lambda : client_exit())
		
		self.insertBottomButton.configure(command = 
			lambda: insert_tBox(self.afterTextBox, self.beforeTextBox.get("1.0", END)))

		self.specialCharButton.configure(command = 
			lambda: get_ascii(self.afterTextBox, self.beforeTextBox.get("1.0",END)))

	def place_buttons(self):
		self.test_button.place(x=10, y=10)
		self.insertBottomButton.place(x=10, y=40)
		self.specialCharButton.place(x=10,y=70)

