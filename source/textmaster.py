from tkinter import *
import tkinter.messagebox as tkmb
from tkinter import ttk
import os
import sys

def setting():
	settingWin = Frame(root)
	settingWin.pack()
	Label(settingWin, text = " ").pack()
	ttk.Label(settingWin, text = "Theme:").pack()

	def deTheme():
		s.theme_use('default')

	defaultB = ttk.Button(settingWin, text = "default", command = deTheme)
	defaultB.pack()

	def clTheme():
		s.theme_use('classic')

	classicB = ttk.Button(settingWin, text = "classic", command = clTheme)
	classicB.pack()

	def alTheme():
		s.theme_use('alt')

	altB = ttk.Button(settingWin, text = "alt", command = alTheme)
	altB.pack()

	def claTheme():
		s.theme_use('clam')

	clamB = ttk.Button(settingWin, text = "clam", command = claTheme)
	clamB.pack()

	def aqTheme():
		s.theme_use('aqua')

	aquaB = ttk.Button(settingWin, text = "aqua", command = aqTheme)
	aquaB.pack()

	Label(settingWin, text = " ").pack()

	def closeSettings():
		settingWin.destroy()

	closeBttn = ttk.Button(settingWin, text = "Close", command = closeSettings)
	closeBttn.pack()

def save():
	textGot = text.get('1.0', 'end')
	saveFrame = Frame(root)
	saveFrame.configure(background = "#4b4f51")
	saveFrame.pack(side = BOTTOM)
	ttk.Label(saveFrame, text = "File Name:").pack()
	fileNameEn = ttk.Entry(saveFrame, textvariable = fileNameVar)
	fileNameEn.pack()

	def done():
		fileName = fileNameVar.get()
		newFile = open(fileName, 'w')
		newFile.write(textGot)
		newFile.close()
		tkmb.showinfo("Text Master", "Your file has been saved as: " + fileName)
		saveFrame.destroy()

	doneB = ttk.Button(saveFrame, text = "Done", command = done)
	doneB.pack()

def quit():
	sys.exit(0)

root = Tk()
root.title('Text Master v.1')
root.configure(background = "#4b4f51")

fileNameVar = StringVar()

s = ttk.Style()
s.theme_use("clam")

top = Frame(root)
top.pack(side = BOTTOM)

b1 = ttk.Button(top, text = " Save ", command = save)
b1.grid(row = 0, column = 0)

b2 = ttk.Button(top, text = " Quit ", command = quit)
b2.grid(row = 0, column = 1)

textFrame = Frame(root)
textFrame.pack()

text = Text(textFrame, width = 50, height = 20)
text.insert('1.0', "Type here...")
text.pack()

settingsFrame = Frame(root)
settingsFrame.pack()

settingsBttn = ttk.Button(settingsFrame, text = " Settings ", command = setting)
settingsBttn.pack()


root.mainloop()