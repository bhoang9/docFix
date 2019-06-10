#Eventually want to have everything pertaining to the window be 
#compartamentalized

from tkinter import *
from button_functions import *

#buttons
showButton = Button(text="Show", command = lambda: print_entry(entry.get()))

insertBottomButton = Button(text="Top to Bottom", 
	command = lambda: insert_tBox(afterTextBox, beforeTextBox.get("1.0", END)))

insertTopButton = Button(text="Bottom to Top",
	command = lambda: insert_tBox(beforeTextBox, afterTextBox.get("1.0", END)))