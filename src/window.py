#!/usr/bin/python3



# ---------------- UTILS ----------------

#toolkit interface
import tkinter






# ---------------- CLASS ----------------
class Window:

	#create graphical window
	def __init__(self, title, width, height, bg_color):
		self.title    = title
		self.width    = width
		self.height   = height
		self.width_2  = int(width/2)
		self.height_2 = int(height/2)

		#create window
		self.win = tkinter.Tk()
		self.win.title(title)

		#create display
		self.display = tkinter.Canvas(
			self.win,
			width=width,
			height=height,
			background=bg_color
		)
		self.display.pack()

		#add keyboard events
		#self.display.bind('<KeyPress>', Window__KeyPressed, )

		#set focus
		self.display.focus_set()

	def stop(self):
		self.win.destroy()

	#draw
	def point(self, x,y, color):
		self.display.create_line(x,y, x,y, fill=color)

	def rect(x1,y1, x2,y2, color, stroke=None):
		if stroke is None:
			stroke = color
		self.display.create_rectangle(x1,y1, x2,y2, fill=color,outline=stroke)

	def circle(x,y, radius, color, stroke=None):
		if stroke is None:
			stroke = color
		self.display.oval(x,y, radius, radius, fill=color, outline=stroke)

	#display
	def show(self):
		self.display.update()
		self.display.delete(tkinter.ALL)

'''
	#get text
	def getInput(self):
		e = Entry(self.win)
		e.pack()
		e.bind('<Return>', self.getReturn)
		key = ''
		while not (key == 'return'):
			e.focus_set()
			self.update()
		text = e.get()
		e.destroy()
		self.display.focus_set()
		return text
'''
