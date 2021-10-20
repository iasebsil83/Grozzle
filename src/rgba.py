#!/usr/bin/python3



# ---------------- UTILS ----------------

#hex conversions
def to2hex(i):
	h = hex(i)[2:]
	if len(h) == 1:
		return '0' + h
	return h






# ---------------- CLASS ----------------
class RGBA:

	#read from file
	def __init__(self, path, width, height):
		self.path   = path
		self.width  = width
		self.height = height

		#get data
		try:
			f   = open(path, 'rb')
			raw = f.read()
			f.close()

			#parse into 2-dimension array
			self.data = []
			index = 0
			for y in range(height):
				self.data.append([])
				for x in range(width):
					self.data[y].append(
						"#" +
						to2hex( raw[index  ] ) +
						to2hex( raw[index+1] ) +
						to2hex( raw[index+2] )
					)
					index += 4

		#error case
		except (IsADirectoryError, FileNotFoundError):
			print(f"RUNTIME ERROR > rgba.py : readRGBA() : Unable to read file '{path}'.")
			self.data = None

	#display
	def show(self, w):
		for y in range(self.height):
			for x in range(self.width):
				w.point(x,y, self.data[y][x])
