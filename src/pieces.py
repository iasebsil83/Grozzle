#!/usr/bin/python3



# ---------------- IMPORTATIONS ----------------

#system
import os, sys

#random
import random

#sources
sys.path.append( os.getcwd() )
from src.binutils import *






# ---------------- DECLARATIONS ----------------

#sides description
SIDE_UP    = 0
SIDE_DOWN  = 1
SIDE_LEFT  = 2
SIDE_RIGHT = 3
SIDE_WALL      = 0b0001
SIDE_INNER     = 0b0010
SIDE_OUTER     = 0b0100
SIDE_UNDEFINED = 0b1000
SIDE_TYPES = (
	SIDE_WALL,
	SIDE_INNER,
	SIDE_OUTER,
	SIDE_UNDEFINED
)






# ---------------- USEFUL ----------------

#description
def sides_to_description(up, down, left, right):
	return (
		( (up   << 12) & 0b1111_0000_0000_0000 ) |
		( (down <<  8) & 0b0000_1111_0000_0000 ) |
		( (left <<  4) & 0b0000_0000_1111_0000 ) |
		( (right     ) & 0b0000_0000_0000_1111 )
	)

def description_to_sides(desc):
	return [
		(desc & 0b1111_0000_0000_0000) >> 12,
		(desc & 0b0000_1111_0000_0000) >>  8,
		(desc & 0b0000_0000_1111_0000) >>  4,
		(desc & 0b0000_0000_0000_1111)
	]

def getPieceChar(side, type):
	if side == SIDE_UP:
		if type == SIDE_WALL:
			return '-'
		elif type == SIDE_INNER:
			return 'v'
		elif type == SIDE_OUTER:
			return '^'
		elif type == SIDE_UNDEFINED:
			return '?'
		else:
			return '#'

	elif side == SIDE_DOWN:
		if type == SIDE_WALL:
			return '-'
		elif type == SIDE_INNER:
			return '^'
		elif type == SIDE_OUTER:
			return 'v'
		elif type == SIDE_UNDEFINED:
			return '?'
		else:
			return '#'

	elif side == SIDE_LEFT:
		if type == SIDE_WALL:
			return '|'
		elif type == SIDE_INNER:
			return '>'
		elif type == SIDE_OUTER:
			return '<'
		elif type == SIDE_UNDEFINED:
			return '?'
		else:
			return '#'

	elif side == SIDE_RIGHT:
		if type == SIDE_WALL:
			return '|'
		elif type == SIDE_INNER:
			return '<'
		elif type == SIDE_OUTER:
			return '>'
		elif type == SIDE_UNDEFINED:
			return '?'
		else:
			return '#'

	#error case
	return '#'






# ---------------- CLASS ----------------
class Piece:

	#constructor
	def __init__(self, up=None, down=None, left=None, right=None):

		#set sides
		self.up    = up    if (up    is not None) else SIDE_TYPES[random.randint(0,2)]
		self.down  = down  if (down  is not None) else SIDE_TYPES[random.randint(0,2)]
		self.left  = left  if (left  is not None) else SIDE_TYPES[random.randint(0,2)]
		self.right = right if (right is not None) else SIDE_TYPES[random.randint(0,2)]

		#set description
		self.desc = sides_to_description(
			self.up,
			self.down,
			self.left,
			self.right
		)

	#display
	def print(self):
		print("    ." + getPieceChar(SIDE_UP,   self.up  ) + ".")
		print("    "  + getPieceChar(SIDE_LEFT, self.left) + " " + getPieceChar(SIDE_RIGHT, self.right) + " (" + printOn16b(self.desc) + ")")
		print("    '" + getPieceChar(SIDE_DOWN, self.down))
