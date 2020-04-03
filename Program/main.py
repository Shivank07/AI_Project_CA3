import random                  # Add the functions that use the random 
import sys                     # Add the sleep () function -> To put the program to pause for a few seconds
from numpy.lib.financial import rate
from bokeh.colors import color
from numpy.core import cross, dot
from math import acos
from numpy import arange
from time import sleep
from math import *

moves = 0                                      # Number of movements carried out, useful for statistics
FPS = 24                                       # For the visual, number of images per second
Box = None

# Plan the correspondence between the face and the vectors
face  = {'F': (color.red, (0, 0, 1)),
		 'B': (color.orange, (0, 0, -1)),
		 'U': (color.yellow, (0, 1, 0)),
		 'L': (color.blue, (-1, 0, 0)),
		 'D': (color.white, (0, -1, 0)),
		 'R': (color.green, (1, 0, 0))}


# Put the colors on each small cube, face by face.
fcolors = []
for face_color, axis in face.values():
	for x in (-1, 0, 1):
		for y in (-1, 0, 1):

			
# Start with all the face colors up, then turn them
			f_color = Box(color=face_color, pos=(x, y, 1.5),
						  length=0.98, height=0.98, width=0.05)
			cos_angle = dot((0, 0, 1), axis)
			pivot = (cross((0, 0, 1), axis) if cos_angle == 0 else (1, 0, 0))
			f_color.rotate(angle=acos(cos_angle), axis=pivot, origin=(0, 0, 0))
			fcolors.append(f_color)


# Rotation of parts of the cube in 3 dimensions
def rotate(k):
	if k[0] in face:
		face_color, axis = face[k[0]]
		angle = ((pi / 2) if len(k)>1 else -pi / 2)
		for r in arange(0, angle, angle / FPS):
			rate(FPS)
			for f_color in fcolors:
				if dot(f_color.pos, axis) > 0.5:
					f_color.rotate(angle=angle / FPS, axis=axis,
								   origin=(0, 0, 0))
	elif k[0] == 'E':
		axis = (0, 0.5, 0)
		angle = ((pi / 2) if len(k)>1 else -pi / 2)
		for r in arange(0, angle, angle / FPS):
			rate(FPS)
			for f_color in fcolors:
				f_color.rotate(angle=angle / FPS, axis=axis,origin=(0, 0, 0))


# d = Down     
# u = Up	  
# f = Face   
# b = Back  
# r = Right 
# l = Left  

# 'w' = White  
# 'y' = Yellow 
# 'r' = Red	
# 'o' = Orange 
# 'g' = Green 
# 'b' = Blue  

#Centres
d   = 'w' 
u   = 'y' 
f   = 'r' 
b   = 'o' 
r   = 'g' 
l   = 'b' 



# Aretes, the name of the variables defines their position on the cube
# Initialize face = {'face' : 'cube color'}
uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
	 
ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}



# Function to make movements
def movement(face, show=1):


	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	global moves
	moves += 1
	if show == 1:
		sys.stdout.write(face + ", ")   # Displays the movement followed by a comma

	if face == "R":   # If the movement indicates is R
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r'],  = \
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r']

		ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'], fr['f'], fr['r'],  = \
		fr['f'], fr['r'], ur['u'], ur['r'], br['b'], br['r'], dr['d'], dr['r'] 
		rotate("R")


	if face == "R'":   # If the movement indicates is R '
		dfr['f'], dfr['d'], dfr['r'], ufr['f'], ufr['u'], ufr['r'], ubr['b'], ubr['u'], ubr['r'], dbr['b'], dbr['d'], dbr['r'], = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dfr['d'], dfr['f'], dfr['r']
		
		ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r'], br['b'], br['r'],  = \
		br['b'], br['r'], ur['u'], ur['r'], fr['f'], fr['r'], dr['d'], dr['r']
		rotate("R'")


	if face == "U":  # If the movement indicates is U
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']
		
		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']
		rotate("U")


	if face == "U'": # ...
		ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f'],  = \
		ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l']

		ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
		uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'], ur['u'], ur['r']
		rotate("U'")


	if face == "D":
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f'],  = \
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']

		dr['d'], dr['r'], df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'],  = \
		df['d'], df['f'], dl['d'], dl['l'], db['d'], db['b'], dr['d'], dr['r']
		rotate("D")


	if face == "D'":
		dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

		df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
		dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']
		rotate("D'")


	if face == "L'":
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l']

		ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'], fl['f'], fl['l'],  = \
		fl['f'], fl['l'], ul['u'], ul['l'], bl['b'], bl['l'], dl['d'], dl['l'] 
		rotate("L'")


	if face == "L":
		dfl['f'], dfl['d'], dfl['l'], ufl['f'], ufl['u'], ufl['l'], ubl['b'], ubl['u'], ubl['l'], dbl['b'], dbl['d'], dbl['l'], = \
		ufl['u'], ufl['f'], ufl['l'], ubl['u'], ubl['b'], ubl['l'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l']
		
		ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l'], bl['b'], bl['l'],  = \
		bl['b'], bl['l'], ul['u'], ul['l'], fl['f'], fl['l'], dl['d'], dl['l']
		rotate("L")


	if face == "F": 
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d']
		
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'],  = \
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f']
		rotate("F")


	if face == "F'":
		ufl['l'], ufl['f'], ufl['u'], ufr['r'], ufr['f'], ufr['u'], dfr['r'], dfr['f'], dfr['d'], dfl['l'], dfl['f'], dfl['d'],  = \
		ufr['u'], ufr['f'], ufr['r'], dfr['d'], dfr['f'], dfr['r'], dfl['d'], dfl['f'], dfl['l'], ufl['u'], ufl['f'], ufl['l']
		
		fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f'], uf['u'], uf['f'],  = \
		uf['u'], uf['f'], fl['l'], fl['f'], df['d'], df['f'], fr['r'], fr['f']
		rotate("F'")


	if face == "B'":	
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l'],  = \
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d']
		
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'],  = \
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b']
		rotate("B'")


	if face == "B":
		ubl['l'], ubl['b'], ubl['u'], ubr['r'], ubr['b'], ubr['u'], dbr['r'], dbr['b'], dbr['d'], dbl['l'], dbl['b'], dbl['d'],  = \
		ubr['u'], ubr['b'], ubr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], ubl['u'], ubl['b'], ubl['l']
		
		bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b'], ub['u'], ub['b'],  = \
		ub['u'], ub['b'], bl['l'], bl['b'], db['d'], db['b'], br['r'], br['b']
		rotate("B")



def mix(move=25, show=1):

	moveList = ["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'"]

	i=0
	for i in range(move):
		random = random.randint(0,11)
		movement(moveList[random], 0)
		if show == 1:
			sys.stdout.write(str(moveList[random]).upper()+ " ")
	if show == 1:
		print("\n\n**Cube mixed !**")



def cube():
	print("\n\t" + ubl['u'] + ub['u'] + ubr['u'] + "\n\t" + \
				ul['u'] + u + ur['u'] + "\n\t" + \
				ufl['u'] + uf['u'] + ufr['u'] + "\n" + \

				ubl['l'] + ul['l'] + ufl['l'] + " "	 + ufl['f'] + uf['f'] + ufr['f'] + " "	   + ufr['r'] + ur['r'] + ubr['r'] + " "	   + ubr['b'] + ub['b'] + ubl['b'] + "\n" + \
				bl['l'] + l + fl['l'] + " "			 + fl['f'] + f + fr['f'] + " "			   + fr['r'] + r + br['r'] + " "			   + br['b'] + b + bl['b'] + " " + "\n" + \
				dbl['l'] + dl['l'] + dfl['l'] + " "	  + dfl['f'] + df['f'] + dfr['f'] + " "	  + dfr['r'] + dr['r'] + dbr['r'] + " "	   + dbr['b'] + db['b'] + dbl['b'] + "\n\t" + \

				dfl['d'] + df['d'] + dfr['d'] + "\n\t" + dl['d'] + d + dr['d'] + "\n\t" + dbl['d'] + db['d'] + dbr['d'] + "\n")

	print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")



def turnCube(show=1):  #from right to left
	global d, u, f, b, r, l

    # D'
	dfr['d'], dfr['f'], dfr['r'], dbr['d'], dbr['b'], dbr['r'], dbl['d'], dbl['b'], dbl['l'], dfl['d'], dfl['f'], dfl['l'],  = \
	dbr['d'], dbr['r'], dbr['b'], dbl['d'], dbl['l'], dbl['b'], dfl['d'], dfl['l'], dfl['f'], dfr['d'], dfr['r'], dfr['f']

	df['d'], df['f'], dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'],  = \
	dr['d'], dr['r'], db['d'], db['b'], dl['d'], dl['l'], df['d'], df['f']

	# U
	ufr['u'], ufr['f'], ufr['r'], ubr['u'], ubr['b'], ubr['r'], ubl['u'], ubl['b'], ubl['l'], ufl['u'], ufl['f'], ufl['l'],  = \
	ubr['u'], ubr['r'], ubr['b'], ubl['u'], ubl['l'], ubl['b'], ufl['u'], ufl['l'], ufl['f'], ufr['u'], ufr['r'], ufr['f']
	
	ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l'], ub['u'], ub['b'],  = \
	ub['u'], ub['b'], ur['u'], ur['r'], uf['u'], uf['f'], ul['u'], ul['l']

	# E'
	fl['f'], fl['l'], fr['f'], fr['r'], br['b'], br['r'], bl['b'], bl['l']  = \
	fr['r'], fr['f'], br['r'], br['b'], bl['l'], bl['b'], fl['l'], fl['f']

	f, r, b, l = \
	r, b, l, f

	rotate("E")

	if show == 1:
		print("** Turn the cube **")



def reset():

	#Centres
	d   = 'w' 
	u   = 'y' 
	f   = 'r' 
	b   = 'o' 
	r   = 'g' 
	l   = 'b' 
	

#names of the variables define their position on the cube
#exp= {'face/direction' : 'cube color'}
	uf = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	ur = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	ub = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	ul = {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	df = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} 
	dr = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} 
	db = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} 
	dl = {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} 
	fr = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	fl = {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	br = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	bl = {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
		 
	ufr = {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} 
	ufl = {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	ubr = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	ubl = {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} 
	dfr = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} 
	dfl = {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} 
	dbr = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} 
	dbl = {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}



def solve_white(s=1):

	if s == 1:
		print("\n ** Construction of the white cross: **\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	list = ['r', 'g', 'o', 'b']

	for i in list:
		if dr['d'] == 'w' and dr['r'] == i:
			movement("R", s)
			movement("R", s)
			movement("U", s)
			movement("F", s)
			movement("F", s)

		elif db['d'] == 'w' and db['b'] == i:
			movement("B", s)
			movement("B", s)
			movement("U", s)
			movement("U", s)
			movement("F", s)
			movement("F", s)

		elif dl['d'] == 'w' and dl['l'] == i:
			movement("L", s)
			movement("L", s)
			movement("U'", s)
			movement("F", s)
			movement("F", s)

		elif fr['f'] == 'w' and fr['r'] == i:
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("F", s)
			movement("F", s)

		elif fl['f'] == 'w' and fl['l'] == i:
			movement("L'", s)
			movement("U'", s)
			movement("L", s)
			movement("F", s)
			movement("F", s)

		elif br['b'] == 'w' and br['r'] == i:
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("F", s)
			movement("F", s)

		elif bl['b'] == 'w' and bl['l'] == i:
			movement("L", s)
			movement("U'", s)
			movement("L'", s)
			movement("F", s)
			movement("F", s)

		elif uf['u'] == 'w' and uf['f'] == i:
			movement("F", s)
			movement("F", s)

		elif ur['u'] == 'w' and ur['r'] == i:
			movement("U", s)
			movement("F", s)
			movement("F", s)

		elif ul['u'] == 'w' and ul['l'] == i:
			movement("U'", s)
			movement("F", s)
			movement("F", s)

		elif ub['u'] == 'w' and ub['b'] == i:
			movement("U", s)
			movement("U", s)
			movement("F", s)
			movement("F", s)

		elif dr['d'] == i and dr['r'] == 'w':
			movement("R", s)
			movement("F", s)

		elif db['d'] == i and db['b'] == 'w':
			movement("B", s)
			movement("D", s)
			movement("R", s)
			movement("D'", s)

		elif dl['d'] == i and dl['l'] == 'w':
			movement("L'", s)
			movement("F'", s)

		elif fr['f'] == i and fr['r'] == 'w':
			movement("F", s)

		elif fl['f'] == i and fl['l'] == 'w':
			movement("F'", s)

		elif br['b'] == i and br['r'] == 'w':
			movement("B", s)
			movement("U", s)
			movement("U", s)
			movement("B'", s)
			movement("F", s)
			movement("F", s)

		elif bl['b'] == i and bl['l'] == 'w':
			movement("B'", s)
			movement("U", s)
			movement("U", s)
			movement("B", s)
			movement("F", s)
			movement("F", s)

		elif uf['u'] == i and uf['f'] == 'w':
			movement("U'", s)
			movement("R'", s)
			movement("F", s)
			movement("R", s)

		elif ur['u'] == i and ur['r'] == 'w':
			movement("R'", s)
			movement("F", s)
			movement("R", s)

		elif ul['u'] == i and ul['l'] == 'w':
			movement("L", s)
			movement("F'", s)
			movement("L'", s)

		elif ub['u'] == i and ub['b'] == 'w':
			movement("U", s)
			movement("R'", s)
			movement("F", s)
			movement("R", s)

		elif df['d'] == i and df['f'] == 'w':
			movement("F'", s)
			movement("D", s)
			movement("R'", s)
			movement("D'", s)
		
		turnCube(s)



def solve_white(s=1):

	if s == 1:
		print("\n *Create white corners : *\n")
	global d, u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl, ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	list = ["wrg", "wgo", "wob", "wbr"]

	for j in list:
		
		if ufl['u'] in j and ufl['f'] in j and ufl['l'] in j:
			movement("U'", s)

		elif ubl['u'] in j and ubl['b'] in j and ubl['l'] in j:
			movement("U'", s)
			movement("U'", s)

		elif ubr['u'] in j and ubr['b'] in j and ubr['r'] in j:
			movement("U", s)

		elif dfl['d'] in j and dfl['f'] in j and dfl['l'] in j:
			movement("L'", s)
			movement("U'", s)
			movement("L", s)

		elif dbl['d'] in j and dbl['b'] in j and dbl['l'] in j:
			movement("L", s)
			movement("U", s)
			movement("U", s)
			movement("L'", s)

		elif dbr['d'] in j and dbr['b'] in j and dbr['r'] in j:
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)


		if dfr['r'] == 'w' and dfr['d'] in j and dfr['f'] in j:
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)

		if dfr['f'] == 'w' and dfr['d'] in j and dfr['r'] in j:
			movement("F'", s)
			movement("U'", s)
			movement("F", s)
			movement("U", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if ufr['u'] == 'w' and ufr['f'] in j and ufr['r'] in j: 
			movement("R", s)
			movement("U", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)

		if ufr['f'] == 'w' and ufr['u'] in j and ufr['r'] in j:
			movement("U", s)
			movement("R", s)
			movement("U'", s)
			movement("R'", s)

		if ufr['r'] == 'w'and ufr['u'] in j and ufr['f'] in j:
			movement("R", s)
			movement("U", s)
			movement("R'", s)
		
		turnCube(s)

def isfinish():

	global d , u, f, b, r, l, uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl , ufr, ufl, ubr, ubl, dfr, dfl, dbr, dbl
	
	if d  == 'w' and \
	u  == 'y' and \
	f  == 'r' and \
	b  == 'o' and \
	r  == 'g' and \
	l  == 'b' and \
	uf == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	ur == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	ub == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	ul == {'u': 'y', 'd': '', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	df == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': ''} and \
	dr == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': 'g', 'l': ''} and \
	db == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': ''} and \
	dl == {'u': '', 'd': 'w', 'f': '', 'b': '', 'r': '', 'l': 'b'} and \
	fr == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	fl == {'u': '', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	br == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	bl == {'u': '', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	ufr == {'u': 'y', 'd': '', 'f': 'r','b': '', 'r': 'g', 'l': ''} and \
	ufl == {'u': 'y', 'd': '', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	ubr == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	ubl == {'u': 'y', 'd': '', 'f': '', 'b': 'o', 'r': '', 'l': 'b'} and \
	dfr == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': 'g', 'l': ''} and \
	dfl == {'u': '', 'd': 'w', 'f': 'r', 'b': '', 'r': '', 'l': 'b'} and \
	dbr == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': 'g', 'l': ''} and \
	dbl == {'u': '', 'd': 'w', 'f': '', 'b': 'o', 'r': '', 'l': 'b'}:

		return 1
	else : return 0



def solve_other(s=1):   # Resolve the second one

	if s == 1:
		print("\n *Creation of the second one :*\n")
	global uf, ur, ub, ul, df, dr, db, dl, fr, fl, br, bl
	list = ['rg', 'go', 'ob', 'br'] # Colors of edges by binomial, each letter represents a color, for example: 'rg' means red-green 

	for i in list:   # This line involves a loop, which means "for each element" i "in the list" list "

		if fl['f'] in i and fl['l'] in i:
			movement("F", s)
			movement("U", s)
			movement("F'", s)
			movement("U'", s)
			movement("L'", s)
			movement("U'", s)
			movement("L", s)

		if br['b'] in i and br['r'] in i:
			turnCube(s)
			turnCube(s)
			movement("F", s)
			movement("U", s)
			movement("F'", s)
			movement("U'", s)
			movement("L'", s)
			movement("U'", s)
			movement("L", s)
			turnCube(s)
			turnCube(s)

		if bl['b'] in i and bl['l'] in i:
			turnCube(s)
			turnCube(s)
			turnCube(s)
			movement("F", s)
			movement("U", s)
			movement("F'", s)
			movement("U'", s)
			movement("L'", s)
			movement("U'", s)
			movement("L", s)
			turnCube(s)

		if fr['r'] is i[0] and fr['f'] in i:
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("U'", s)
			movement("R", s)
			movement("U'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if uf['f'] is i[0] and uf['u'] in i:
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if uf['u'] is i[0] and uf['f'] in i:
			movement("U'", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R", s)

		if ur['u'] is i[0] and ur['r'] in i:
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R", s)

		if ur['r'] is i[0] and ur['u'] in i:
			movement("U", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if ub['b'] is i[0] and ub['u'] in i:
			movement("U'", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if ub['u'] is i[0] and ub['b'] in i:
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R", s)

		if ul['l'] is i[0] and ul['u'] in i:
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("F'", s)
			movement("U'", s)
			movement("F", s)

		if ul['u'] is i[0] and ul['l'] in i:
			movement("U", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U'", s)
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R", s)

		if fr['f'] is i[0] and fr['r'] in i and s == 1:
			print("Arete bien mise !")

		turnCube(s)



def solve_yellow(s=1):
	if s == 1:
		print("\n *Creation of yellow one :\n")

	global uf, ur, ub, ul

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] != 'y':  # If yellow dot then:
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if uf['u'] != 'y' and  ub['u'] != 'y' and ur['u'] == 'y' and ul['u'] == 'y':  # If yellow line well put:
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if ur['u'] != 'y' and  ul['u'] != 'y' and uf['u'] == 'y' and ub['u'] == 'y':   # If yellow line but poorly placed:
		movement("U", s)     # Simple rotation of the top face to properly put the yellow line
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if uf['u'] != 'y' and ur['u'] != 'y' and ub['u'] == 'y' and ul['u'] == 'y':    # If yellow "L" properly put:
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if uf['u'] != 'y' and ur['u'] == 'y' and ub['u'] == 'y' and ul['u'] != 'y':    # If improperly put "L" yellow:
		movement("U'", s)      # Simple rotation of the top face to put the yellow "L"
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if uf['u'] == 'y' and ur['u'] == 'y' and ub['u'] != 'y' and ul['u'] != 'y':     # If improperly put "L" yellow:
		movement("U", s)	    # Simple rotation of the top face to put the yellow "L"
		movement("U", s)	
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	if uf['u'] == 'y' and ur['u'] != 'y' and ub['u'] != 'y' and ul['u'] == 'y': 
		movement("U", s)	
		movement("R'", s)
		movement("U'", s)
		movement("F'", s)
		movement("U", s)
		movement("F", s)
		movement("R", s)

	
# Cross built

	#Setting up colors:
	loop = 1       # Variable which determines if yes (0) or not (1) the colors are in their places
	while loop:    # Loop "as long as loop is equal to 1"
			if uf['f'] == 'r' and ur['r'] == 'g':
				movement("U", s)
				movement("U", s)

			elif ul['l'] == 'r' and uf['f'] == 'g':
				movement("U", s)

			elif ur['r'] == 'r' and ub['b'] == 'g':
				movement("U'", s)

			if uf['f'] == 'g' and ur['r'] == 'o':
				movement("U", s)
				movement("U", s)

			elif ul['l'] == 'g' and uf['f'] == 'o':
				movement("U", s)

			elif ur['r'] == 'g' and ub['b'] == 'o':
				movement("U'", s)

			if uf['f'] == 'o' and ur['r'] == 'b':
				movement("U", s)
				movement("U", s)

			elif ul['l'] == 'o' and uf['f'] == 'b':
				movement("U", s)

			elif ur['r'] == 'o' and ub['b'] == 'b':
				movement("U'", s)

			if uf['f'] == 'b' and ur['r'] == 'r':
				movement("U", s)
				movement("U", s)

			elif ul['l'] == 'b' and uf['f'] == 'r':
				movement("U", s)

			elif ur['r'] == 'b' and ub['b'] == 'r':
				movement("U'", s)

			# Algorithm
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("R'", s)
			movement("U", s)
			movement("R", s)
			movement("U", s)
			movement("U", s)
			movement("R'", s)

			#Test the cube if the colors can be placed with only "U" movements
			if ul['l'] == 'r' and uf['f'] == 'g' and ur['r'] == 'o' and ub['b'] == 'b':
				movement("U'", s)
			if ul['l'] == 'o' and uf['f'] == 'b' and ur['r'] == 'r' and ub['b'] == 'g':
				movement("U", s)
			if ul['l'] == 'g' and uf['f'] == 'o' and ur['r'] == 'b' and ub['b'] == 'r':
				movement("U", s)
				movement("U", s)
			if ul['l'] == 'b' and uf['f'] == 'r' and ur['r'] == 'g' and ub['b'] == 'o':
				loop = 0     # If the cross and the colors are well set then the program exits the function



def solve_final(s=1):
	if s == 1:
		print("\n *Creation of yellow corners : *\n")

	while 1:    

		if  ('r' in ufr.values() and 'g' in ufr.values()) and \
			('b' in ufl.values() and 'r' in ufl.values()) and \
			('g' in ubr.values() and 'o' in ubr.values()) and \
			('b' in ubl.values() and 'o' in ubl.values()):
				break 

		if 'g' in ubr.values() and 'o' in ubr.values():    # If g (green) and o (orange) are contained in the values ​​of ubr (up-back-right) then:
			movement("U", s)
			movement("U", s)
			movement("R", s)
			movement("U'", s)
			movement("L'", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("L", s)
			movement("U'", s)

		elif 'r' in ufr.values() and 'g' in ufr.values():
			movement("U", s)
			movement("R", s)
			movement("U'", s)
			movement("L'", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("L", s)

		elif 'b' in ubl.values() and 'o' in ubl.values():
			movement("U'", s)
			movement("R", s)
			movement("U'", s)
			movement("L'", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("L", s)
			movement("U", s)
			movement("U", s)

		elif 'b' in ufl.values() and 'r' in ufl.values():
			movement("R", s)
			movement("U'", s)
			movement("L'", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("L", s)
			movement("U", s)

		else:    # If no side is well placed: / Otherwise:
			movement("U", s)
			movement("R", s)
			movement("U'", s)
			movement("L'", s)
			movement("U", s)
			movement("R'", s)
			movement("U'", s)
			movement("L", s)

	while 1:
		if ufr['u'] == 'y':    # If the yellow color of cubie is on top of the cube then:
			if isfinish()():     # If the cube is solved then:
				break 

			movement("U'", s)   # Go to the next cubie

		if ufr['r'] == 'y':    # If the yellow color of cubie is on the right of the cube then:
			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)

			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)

		if ufr['f'] == 'y':    # If the yellow color of cubie is on the front of the cube then:
			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)

			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)

			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)

			movement("R'", s)
			movement("D'", s)
			movement("R", s)
			movement("D", s)


##### Mixing the cube #####
print("Mixing the cube :\n")
mix() 
cube() 
print("Mixing of the finished cube !\n")
sleep(5) 


##### Resolution #####

if isfinish()():    # If the cube is solved:
	print("Finished in " + str(moves) + " moves.")
	quit()

solve_white() 

if isfinish()(): 
	print("Finished in " + str(moves) + " moves.")
	quit()

solve_white()    # Resolution of white corners

cube()           # Displays the cube

if isfinish()(): 
	print("Finished in"  + str(moves) + " moves.")
	quit()

solve_other()      # Resolution of the second line

cube() 

if isfinish()():
	print("Finished in " + str(moves) + " moves.")
	quit()

solve_yellow() 

cube() 

if isfinish()(): 
	print("Finished in" + str(moves) + " moves.")
	quit()

solve_final()     # Resolution of the corners of the yellow face

cube() 

if isfinish()(): 
	print("Finished in" + str(moves) + " moves.")
	quit()

cube() 
