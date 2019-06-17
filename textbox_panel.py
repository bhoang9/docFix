from tkinter import *

class textbox_panel:

	def __init__(self, root, frame):

		self.root = root
		self.frame = frame

		self.beforeTextBox = None
		self.afterTextBox = None

		self.init_textboxes()

	def get_before_textbox(self):
		return self.beforeTextBox

	def get_after_textbox(self):
		return self.afterTextBox

	def init_textboxes(self):

		self.beforeTextBox = Text(self.frame, height=18,width=80, borderwidth=2, relief="solid")
		self.afterTextBox = Text(self.frame, height=18, width=80, borderwidth=2, relief="solid")

		self.beforeTextBox.pack(side = TOP, fill = BOTH, expand = True)
		self.afterTextBox.pack(side = BOTTOM, fill = BOTH, expand = True)