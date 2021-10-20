#!/usr/bin/python3



# ---------------- USEFUL ----------------

#binary text
def printOnNbits(i, n):
	b = bin(i)[2:]
	return "0"*(n-len(b)) + b

def printOnNdec(i,n):
	d = str(i)
	return "0"*(n-len(d)) + d

def printOn16b(i):
	text     = bin(i)[2:]
	text_len = len(text)
	if text_len > 16:
		return "########"
	elif text_len == 16:
		return         text[:4] + ' ' + text[4:8] + ' ' + text[8:12] + ' ' + text[12:]
	elif text_len == 15:
		return "0"   + text[:3] + ' ' + text[3:7] + ' ' + text[7:11] + ' ' + text[11:]
	elif text_len == 14:
		return "00"  + text[:2] + ' ' + text[2:6] + ' ' + text[6:10] + ' ' + text[10:]
	elif text_len == 13:
		return "000" + text[:1] + ' ' + text[1:5] + ' ' + text[5:9]  + ' ' + text[9:]
	return "........"



#array
def to16bArray(i):
	return [
		(i & 0b1000_0000_0000_0000) != 0,
		(i & 0b0100_0000_0000_0000) != 0,
		(i & 0b0010_0000_0000_0000) != 0,
		(i & 0b0001_0000_0000_0000) != 0,

		(i & 0b0000_1000_0000_0000) != 0,
		(i & 0b0000_0100_0000_0000) != 0,
		(i & 0b0000_0010_0000_0000) != 0,
		(i & 0b0000_0001_0000_0000) != 0,

		(i & 0b0000_0000_1000_0000) != 0,
		(i & 0b0000_0000_0100_0000) != 0,
		(i & 0b0000_0000_0010_0000) != 0,
		(i & 0b0000_0000_0001_0000) != 0,

		(i & 0b0000_0000_0000_1000) != 0,
		(i & 0b0000_0000_0000_0100) != 0,
		(i & 0b0000_0000_0000_0010) != 0,
		(i & 0b0000_0000_0000_0001) != 0
	]
