#!/usr/bin/python3



# ---------------- IMPORTATIONS ----------------

#system
import os, sys

#tkinter
from tkinter import PhotoImage

#sources
sys.path.append( os.getcwd() )
from src.pieces import *






# ---------------- DECLARATIONS ----------------

#2-power
power2 = (1,2,4,8,16,32,64,128,256,512,1024,2048,4096)






# ---------------- USEFUL ----------------

#description
def subImage(image, px,py, width,height):
	subImg  = PhotoImage(width=width, height=height)
	subData = ""
	for y in range(height):
		subData += " { "
		for x in range(width):
			subData += "#%02x%02x%02x " % image.get(px + x, py + y)
		subData += "}"

	subImg.put(subData)
	return subImg






# ---------------- CLASS ----------------
class Puzzle:

	#constructor
	def __init__(self, path, rowNbr, colNbr):

		#error cases
		if rowNbr not in power2:
			print("FATAL ERROR > src/puzzle.py : __init__() : rowNbr can only be a small power of 2 (got " + rowNbr + ").")
			exit(1)
		if colNbr not in power2:
			print("FATAL ERROR > src/puzzle.py : __init__() : colNbr can only be a small power of 2 (got " + colNbr + ").")
			exit(1)

		#set image
		self.path  = path
		try:
			self.fullImage = PhotoImage(file=path)
			self.width     = self.fullImage.width()
			self.height    = self.fullImage.height()
			self.width_2   = int(self.width/2)
			self.height_2  = int(self.height/2)
		except RuntimeError:
			print("FATAL ERROR > src/puzzle.py : __init__() : Unable to allocate puzzle image without having first created a tkinter window.")
			exit(1)

		#set attributes
		self.rowNbr        = rowNbr
		self.colNbr        = colNbr
		self.piecesNbr     = rowNbr*colNbr
		self.pieces        = []
		self.pieceWidth    = int(self.width/colNbr)
		self.pieceHeight   = int(self.height/rowNbr)
		self.pieceWidth_2  = int(self.pieceWidth/2)
		self.pieceHeight_2 = int(self.pieceHeight/2)

		#generate pieces
		for y in range(rowNbr):
			self.pieces.append([])
			for x in range(colNbr):
				self.pieces[y].append(
					Piece(
						SIDE_WALL,
						SIDE_WALL,
						SIDE_WALL,
						SIDE_WALL,
						subImage(
							self.fullImage,
							x*self.pieceWidth, y*self.pieceHeight,
							  self.pieceWidth,   self.pieceHeight
						)
					)
				)

		#TEMP <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		SHIFT = 10
		self.width       += self.colNbr * SHIFT
		self.height      += self.rowNbr * SHIFT
		self.width_2      = self.width/2
		self.height_2     = self.height/2
		self.pieceWidth  += SHIFT
		self.pieceHeight += SHIFT

	#display
	def show(self, win, px, py):

		#centralize puzzle
		px -= self.width_2
		py -= self.height_2

		#show pieces
		for y in range(self.rowNbr):
			for x in range(self.colNbr):
				self.pieces[y][x].show(
					win,
					px + x*self.pieceWidth  + self.pieceWidth_2,
					py + y*self.pieceHeight + self.pieceHeight_2,
				)
