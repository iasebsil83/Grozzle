#!/usr/bin/python3



# ---------------- IMPORTATIONS ----------------

#system
import os, sys

#time
from time import sleep

#PhotoImage
from tkinter import PhotoImage

#sources
sys.path.append( os.getcwd() )
from src.rgba import *






# ---------------- GROVER ----------------

#circuit
def startup(w):

	#show startup image
	#startup_img = RGBA("sprites/rgba/QuantumNeon_1080x640.rgba", 1080,640)
	#startup_img.show(w, w.width_2, w.height_2)
	startup_img = PhotoImage(file="sprites/png/QuantumNeon.png")
	w.display.create_image(w.width_2, w.height_2, image=startup_img)
	w.show()

	#delay
	sleep(0.5)
