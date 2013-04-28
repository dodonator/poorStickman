#!/usr/bin/env python

# 22 verschiedene Tasten zu bedienen

# Include the PySFML extension
from PySFML import *
import time
import os
import datetime
import getpass
import random
# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "Messerwerfer mit Joystick")
# Create a graphical string to display
weapon = sf.String("PNG SFML")
fps = sf.String("0")
fps.Move(400,0)
fpsCounter = 0
counterTime = time.time()
# window.SetFramerateLimit(60)
schrift = sf.String('    ')
schrift2 = sf.String('    ')

running = True
joyId = 0
texture = sf.Image()
texture2 = sf.Image()
texture3 = sf.Image()
texture4 = sf.Image()
texture.LoadFromFile(".messer.png")
texture2.LoadFromFile(".stickman2.png")
texture3.LoadFromFile(".BlueBlood.png")
texture4.LoadFromFile(".windowsBlau.png")
weapon = sf.Sprite(texture)
weapon.Move(150,150)
text2 = sf.Sprite(texture2)
text3 = sf.Sprite(texture3)
text4 = sf.Sprite(texture4)
# Start the game loop
running = True
unsichtbarkeit = False
gStatus = 'Gesund'
window.ShowMouseCursor(False)
xcollide = False
ycollide = False
collision = False
spaceNumbers = 0
while running:
	schrift.SetColor(sf.Color.Red)
	schrift2.SetColor(sf.Color.Red) 
	if gStatus == 'Gesund':
		schrift = sf.String('    ')
	if gStatus == 'Verletzt':
		schrift = sf.String('Sie sind verletzt! \n Lassen sie sich wiederbeleben!')
	if collision == True:
		schrift2 = sf.String('\n \n Treffer!')
	if collision == False:
		schrift2 = sf.String(' ')
	inp = window.GetInput()
	fpsCounter += 1
	if time.time() -  counterTime >= 1:
		fps.SetText(str(fpsCounter))
		fpsCounter = 0
		counterTime = time.time()
	event = sf.Event() 
	xcollide = False
	ycollide = False
	collision = False
	reNum = 0
	while window.GetEvent(event):		
		text3.SetPosition(800,600)
		# schrift = sf.String('    ')
		if event.Type == sf.Event.Closed or event.Key.Code == 256: # ESCAPE
			running = False
		if event.Type == sf.Event.KeyPressed:
			#http://www.sfml-dev.org/documentation/1.6/namespacesf_1_1Key.php
			if event.Key.Code == 291: #left Bewegung Waffe nach links (Pfeiltaste)
				weapon.Move(-10,0)
			elif event.Key.Code == 292: #right Bewegung Waffe nach rechts (Pfeiltaste)
				weapon.Move(10,0)
			elif event.Key.Code == 293: #up Bewegung Waffe nach oben (Pfeiltaste)
				weapon.Move(0,-10)
			elif event.Key.Code == 294: #down Bewegung Waffe nach unten (Pfeiltaste)
				weapon.Move(0,10)
			if event.Key.Code == 97: #left A Bewegung Stickman nach Links
				text2.Move(-5,0)
			elif event.Key.Code == 100: #right D Bewegung Stickman nach Rechts
				text2.Move(5,0)
			elif event.Key.Code == 119: #up W Bewegung Stickman nach Oben
				text2.Move(0,-5)
			elif event.Key.Code == 115: #down D Bewegung Stickman nach unten
				text2.Move(0,5)
			if event.Key.Code == 49: # 1: Waffe 180 Grad Drehung
				weapon.Rotate(180)
			elif event.Key.Code == 50: # 2: Waffe 90 Grad Drehung
				weapon.Rotate(90)
			elif event.Key.Code ==51:  # 3: Waffe 60 Grad Drehung
				weapon.Rotate(60)
			elif event.Key.Code == 107: # K: Waffe 120 Grad Drehung
				weapon.Rotate(120)
			if event.Key.Code == 280: # Tab: Stickman 90 Grad Drehung gegen den Uhrzeigersinn
				text2.Rotate(90)
			elif event.Key.Code == 258: # Shift: Stickman 90 Grad Drehung mit dem Uhrzeigersinn
				text2.Rotate(-90)
			if event.Key.Code == sf.Key.Q: #lefrrot q
				weapon.Rotate(-5)
			elif event.Key.Code == sf.Key.E: #rightrot e
				weapon.Rotate(+5)
			if event.Key.Code == sf.Key.R: #RESSURECT! Wiederbelebung
				if gStatus == 'Verletzt':	
					if unsichtbarkeit == True:
						weapon.Move(150,150)
						texture.LoadFromFile(".messer.png")
						texture2.LoadFromFile(".invStickman.png")
						texture3.LoadFromFile(".BlueBlood.png")
					else:
						weapon.Move(150,150)
						texture.LoadFromFile(".messer.png")
						texture2.LoadFromFile(".stickman2.png")
						texture3.LoadFromFile(".BlueBlood.png")	
					text3.SetPosition(0,0)
					gStatus = 'Gesund'
			elif event.Key.Code == 8 or event.Key.Code == 9:
				texture4.LoadFromFile(".messer2.png")
				text4.SetPosition(random.randint(50, 750), random.randint(50, 550))
			if event.Key.Code == 105: # I: Unsichtbarkeit
				if gStatus == 'Gesund':	
					texture2.LoadFromFile(".invStickman.png")
					unsichtbarkeit = True
			elif event.Key.Code == sf.Key.V: # V: Wiedersichtbarkeit
				if unsichtbarkeit == True:
					texture2.LoadFromFile(".stickman2.png")
					unsichtbarkeit = False
			if event.Key.Code == 277:
				text4.SetPosition(random.randint(50 + spaceNumbers,750 - spaceNumbers),random.randint(50 + spaceNumbers,550 - spaceNumbers))
				texture4.LoadFromFile(".messer2.png")
				text4.Move(5,0)
				spaceNumbers += 1
				if spaceNumbers == 250:
					spaceNumbers = 0
				print '--------' + '\n' + str(spaceNumbers) + '\n--------'
			elif event.Key.Code == 259:
				texture4.LoadFromFile(".windowsBlau.png")
				text4.SetPosition(800,600)
				spaceNumbers = 0
			else:
				print event.Key.Code # So kommt man an die Keys!
		if event.Type == 10:
			print event.MouseMove.X
			x = event.MouseMove.X
			print event.MouseMove.Y
			y = event.MouseMove.Y
			print "----------------"
			weapon.SetPosition(x,y)
		if event.Type == sf.Event.JoyMoved:
			xAchse = inp.GetJoystickAxis(joyId,0)
			yAchse = inp.GetJoystickAxis(joyId,1)
			if xAchse > 0:
				text2.Move(xAchse - 90, 0)
			elif xAchse < 0:
				text2.Move(xAchse + 90, 0)
			elif yAchse > 0:
				text2.Move(0, yAchse - 90)
			elif yAchse < 0:
				text2.Move(0, yAchse + 90)	
		if event.Type == sf.Event.JoyMove:
			xAchse = inp.GetJoystickAxis(joyId,0)
			yAchse = inp.GetJoystickAxis(joyId,1)
			print 'JoyMove'
			if xAchse > 0:
				text2.Move(xAchse - 90, 0)
			elif xAchse < 0:
				text2.Move(xAchse + 90, 0)
			elif yAchse > 0:
				text2.Move(0, yAchse - 90)
			elif yAchse < 0:
				text2.Move(0, yAchse + 90)
		if event.Type == sf.Event.JoyButtonPressed:
			text4.SetPosition(random.randint(50 + spaceNumbers,750 - spaceNumbers),random.randint(50 + spaceNumbers,550 - spaceNumbers))
			texture4.LoadFromFile(".messer2.png")
			print '--------' + '\n' + str(spaceNumbers) + '\n--------'
			if spaceNumbers == 250:
				spaceNumbers = 0
		print event.Type
		if ((weapon.GetPosition()[0]+30 >= text2.GetPosition()[0] and weapon.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (weapon.GetPosition()[0] <= text2.GetPosition()[0]+50 and weapon.GetPosition()[0] >= text2.GetPosition()[0])) or (((weapon.GetPosition()[1]+30 >= text2.GetPosition()[1] and weapon.GetPosition()[1] <= text2.GetPosition()[1]+100) or (weapon.GetPosition()[1] <= text2.GetPosition()[1]+100 and weapon.GetPosition()[1]+30 >= text2.GetPosition()[1]))):
			if (weapon.GetPosition()[0]+30 >= text2.GetPosition()[0] and weapon.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (weapon.GetPosition()[0] <= text2.GetPosition()[0]+50 and weapon.GetPosition()[0] >= text2.GetPosition()[0]):
				xcollide = True			
			if ((weapon.GetPosition()[1]+30 >= text2.GetPosition()[1] and weapon.GetPosition()[1] <= text2.GetPosition()[1]+100) or (weapon.GetPosition()[1] <= text2.GetPosition()[1]+100 and weapon.GetPosition()[1]+30 >= text2.GetPosition()[1])):
				ycollide = True
			if xcollide == True and ycollide == True:
				collision = True
				if collision == True:
					texture.LoadFromFile(".messerBlood.png")
					texture2.LoadFromFile(".stickmanBlood.png")
					texture3.LoadFromFile(".Blood.png")
					text3.SetPosition(random.randint(-10,10)+text2.GetPosition()[0],random.randint(-10,30)+text2.GetPosition()[1]) 
					gStatus = 'Verletzt'
	# Draw the text, and update the window
	window.Clear(sf.Color.Blue)
	window.Draw(weapon)
	window.Draw(text2)
	window.Draw(text3)
	window.Draw(text4)
	window.Draw(fps)
	window.Draw(schrift)
	window.Draw(schrift2)	
	window.Display()
os.system('clear')
print 'Diese Tasten werden unterstuetzt:'
os.system('eog .joytest.JPG &')
# Man koennte Zufallszahlen erzeugen mit:
# 1. spaceNumbers
# 2. Mausposition
# 3. Uhrzeit
# 4. Zufallszahl
# 5. Stickmanposition
# 6. Quersummen

# Dieses Programm ist sehr komplex
# Variablen muessen umbenannt werden
# Funktionen muessen eingebaut werden
