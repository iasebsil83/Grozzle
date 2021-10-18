#!/usr/bin/python3



# ---------------- CLASS ----------------

#initialization
def readRGBA(path, width, height):
	try:
		f    = open(path, 'rb')
		data = f.read()
		f.close()

		#get image data
		image = []

		return image

	#error case
	except (IsADirectoryError, FileNotFoundError):
		print(f"RUNTIME ERROR > rgba.py : readRGBA() : Unable to read file '{path}'.")
