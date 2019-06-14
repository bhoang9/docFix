from tkinter import *

beforeTextBox = Text()
afterTextBox = Text()

class textbox_panel:

	def __init__(self, root, frame):

		self.root = root
		self.frame = frame

		#self.beforeTextBox = None
		#self.afterTextBox = None

		self.init_textboxes()

	def get_before_textbox(self):
		return beforeTextBox

	def get_after_textbox(self):
		return afterTextBox

	def init_textboxes(self):

		beforeTextBox = Text(self.frame, height=18,width=80, borderwidth=2, relief="solid")
		afterTextBox = Text(self.frame, height=18, width=80, borderwidth=2, relief="solid")

		beforeTextBox.pack(side = TOP, fill = BOTH, expand = True)
		afterTextBox.pack(side = BOTTOM, fill = BOTH, expand = True)