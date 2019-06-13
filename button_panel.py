from tkinter import *
from button_functions import *

class button_panel:

	def __init__(self, root, frame):
		self.root = root
		self.frame = frame

		test_button = None

		self.create_buttons()

	def create_buttons(self):

		test_button = Button(self.frame, text="test Button")
		test_button.place(x=10, y=10)

	def define_buttons(self):
		test_button.configure(command = lambda : client_exit())

