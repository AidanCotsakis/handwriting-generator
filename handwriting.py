import numpy as np
from PIL import Image, ImageDraw
import random

tw = 64
th = 128
cw = tw*12
ch = th*6

imw = 1920*5
imh = 1080*5

chars = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0","+","-","=","*","(",")","[","]","{","}","/",".",",",":",";","'",">","<","^","@U","@N","@O","@S","@u","@s","@2","@3","!","?","%","#","|","@<","@>"]

def findMinX(im):
	for y in range(im.shape[1]):
		for x in range(im.shape[0]):
			if im[x][y][3] != 0:
				return y

def findMaxX(im):
	for y in range(im.shape[1]-1, 0, -1):
		for x in range(im.shape[0]):
			if im[x][y][3] != 0:
				return y

def lumocityMask(im):
	for y in range(im.shape[1]):
		for x in range(im.shape[0]):
			a = 255-(im[x][y][0])
			im[x][y][0] = 0
			im[x][y][1] = 0
			im[x][y][2] = 0
			im[x][y][3] = a

	return im

def slpitImage(image, startIdx = 0):
	pIm = Image.open(image).convert("RGBA")
	pIm.thumbnail((cw,ch), Image.Resampling.LANCZOS)
	
	pIm.save("resized.png")

	im = np.array(pIm)

	tiles = [im[x:x+th,y:y+tw] for x in range(0,im.shape[0],th) for y in range(0,im.shape[1],tw)]
	for tile in enumerate(tiles):
		idx = startIdx*3 + tile[0]
		if int(idx/3) < len(chars):

			img = tile[1]

			img = lumocityMask(img)

			minX = findMinX(img)
			maxX = findMaxX(img)

			minX = max(minX, 0)
			maxX = min(maxX, tw-1)

			img = img[0:th,minX:maxX]

			pil_img = Image.fromarray(img)
			pil_img.save(f"chars/char_{int(idx/3)}_{idx%3}.png")

def generateTemplate():
	im = Image.new('RGBA', (cw, ch), (255, 255, 255, 255)) 
	draw = ImageDraw.Draw(im, "RGBA") 
	for i in range(0,ch,th):
		draw.line((0,i,cw,i), fill=(0,0,0), width=2)
		draw.line((0,i+int(th/3),cw,i+int(th/3)), fill=(200,200,200), width=1)
		draw.line((0,i+int(2*th/3),cw,i+int(2*th/3)), fill=(200,200,200), width=1)

	for i in range(0,cw,tw):
		draw.line((i,0,i,ch), fill=(0,0,0), width=2)
	im.save("template.png")

def generateResult(text):

	im = Image.new('RGBA', (imw, imh), (255, 255, 255, 255))
	blank = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

	currx = 0
	curry = 0

	words = text.split(" ")
	for word in words:
		aword = ""
		wordChars = []
		wordGaps = []
		special = False
		for char in word:
			flag = True
			if special:
				special = False
				aword += char
				char = "@" + char
			elif char == "@":
				special = True
				flag = False
			else:
				aword += char
			
			if char == "\n":
				wordChars.append(blank)
				wordGaps.append(0)
				flag = False

			if flag:
				variation = random.randint(0,2)
				idx = chars.index(char)
				charIm = Image.open(f"chars/char_{idx}_{variation}.png")
				wordChars.append(charIm)
				width, height = charIm.size
				wordGaps.append(width-random.randint(1,5))

		wordSize = 0
		for gap in wordGaps:
			wordSize += gap

		if currx + wordSize >= imw:
			currx = 0
			curry += int(2*th/3)

		for i in range(len(wordChars)):
			flag = True
			if aword[i] == "\n":
				currx = 0
				curry += int(2*th/3)
				flag = False

			if flag:
				im.paste(wordChars[i], (currx, curry), wordChars[i])
				currx += wordGaps[i]

		currx += random.randint(40,60)

	im.save("result.png")
