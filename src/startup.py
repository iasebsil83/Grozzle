#!/usr/bin/python3



# ---------------- IMPORTATIONS ----------------

#system
import os, sys

#time
from time import sleep

#PhotoImage
from tkinter import Canvas
from tkinter import PhotoImage






# ---------------- DECLARATIONS ----------------

#dimensions
STARTUP_WIDTH  = 1080
STARTUP_HEIGHT = 640






# ---------------- EXECUTION ----------------

#sequence
def startup(win):

	#show startup image
	startup_img = PhotoImage(file="sprites/QuantumNeon.png")
	win.display.create_image(win.width_2, win.height_2, image=startup_img)
	win.show()

	#delay
	sleep(1)
