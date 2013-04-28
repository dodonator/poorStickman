#!/usr/bin/env python
# Joystick Feature eingebaut!
# Steuerknueppel: Stickman random bewegen
# Tasten: Tux Random bewegen
# Include the PySFML extension
from PySFML import *
import time
import os
import datetime
import getpass
import random
# Create the main window
window = sf.RenderWindow(sf.VideoMode(800, 600), "Messerwerfer!")

# Create a graphical string to display
weapon = sf.String("PNG SFML")
fps = sf.String("0")
fps.Move(400,0)
fpsCounter = 0
counterTime = time.time()


# window.SetFramerateLimit(60)

running = True

texture = sf.Image()
texture2 = sf.Image()
texture3 = sf.Image()
texture4 = sf.Image()
texture.LoadFromFile(".messer.png")
texture2.LoadFromFile(".stickman2.png")
texture3.LoadFromFile(".BlueBlood.png")
texture4.LoadFromFile(".messer2Blood.png")
weapon = sf.Sprite(texture)
weapon.Move(150,150)
text2 = sf.Sprite(texture2)
text3 = sf.Sprite(texture3)
text4 = sf.Sprite(texture4)
text4.SetPosition(random.randint(350,450),random.randint(250,350))
# Start the game loop

running = True

window.ShowMouseCursor(False)
while running:
    fpsCounter +=1
    if time.time() -  counterTime >=1:
        fps.SetText(str(fpsCounter))
        fpsCounter = 0
        counterTime = time.time()

    event = sf.Event() 
    xcollide = False
    ycollide = False
    xcollide2 = False
    ycollide2 = False
    collision = False
    collision2 = False
    reNum = 0
    while window.GetEvent(event):		
		text3.SetPosition(800,600)
		if event.Type == sf.Event.Closed:
			running = False
		elif event.Type == sf.Event.KeyPressed:
			#http://www.sfml-dev.org/documentation/1.6/namespacesf_1_1Key.php
			if event.Key.Code == 291: #left
				weapon.Move(-10,0)
			elif event.Key.Code == 292: #right
				weapon.Move(10,0)
			elif event.Key.Code == 293: #up
				weapon.Move(0,-10)
			elif event.Key.Code == 294: #down
				weapon.Move(0,10)
			elif event.Key.Code == 97: #left
				text2.Move(-5,0)
			elif event.Key.Code == 100: #right
				text2.Move(5,0)
			elif event.Key.Code == 119: #up
				text2.Move(0,-5)
			elif event.Key.Code == 115: #down
				text2.Move(0,5)
			elif event.Key.Code == 49:
				weapon.Rotate(180)
			elif event.Key.Code == 50:
				weapon.Rotate(90)
			elif event.Key.Code ==51:
				weapon.Rotate(60)
			elif event.Key.Code == 107:
				weapon.Rotate(120)
			elif event.Key.Code == 280:
				text2.Rotate(90)
			elif event.Key.Code == 258:
				text2.Rotate(-90)
			elif event.Key.Code == sf.Key.Q: #lefrrot q
				weapon.Rotate(-5)
			elif event.Key.Code == sf.Key.E: #rightrot e
				weapon.Rotate(+5)
			elif event.Key.Code == sf.Key.R: #RESSURECT!
				weapon.Move(150,150)
				texture.LoadFromFile(".messer.png")
				texture2.LoadFromFile(".stickman2.png")
				texture3.LoadFromFile(".BlueBlood.png")
				texture4.LoadFromFile(".messer2Blood.png")
				text3.SetPosition(0,0)  
			else:
				print event.Key.Code
		elif  event.Type == sf.Event.JoyMoved: #15 axis
			text2.SetPosition(random.randint(0, 750), random.randint(0, 500))	
				
		elif  event.Type == 10:

			print event.MouseMove.X
			x = event.MouseMove.X
			print event.MouseMove.Y
			y = event.MouseMove.Y
			print "----------------"
			weapon.SetPosition(x,y)
		
		elif event.Type == sf.Event.JoyButtonPressed:
			if ((text4.GetPosition()[0]+30 >= text2.GetPosition()[0] and text4.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (text4.GetPosition()[0] <= text2.GetPosition()[0]+50 and text4.GetPosition()[0] >= text2.GetPosition()[0])) or (((text4.GetPosition()[1]+30 >= text2.GetPosition()[1] and text4.GetPosition()[1] <= text2.GetPosition()[1]+100) or (text4.GetPosition()[1] <= text2.GetPosition()[1]+100 and text4.GetPosition()[1]+30 >= text2.GetPosition()[1]))):
				if (text4.GetPosition()[0]+30 >= text2.GetPosition()[0] and text4.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (text4.GetPosition()[0] <= text2.GetPosition()[0]+50 and text4.GetPosition()[0] >= text2.GetPosition()[0]):
					xcollide2 = True			
				if ((text4.GetPosition()[1]+30 >= text2.GetPosition()[1] and text4.GetPosition()[1] <= text2.GetPosition()[1]+100) or (text4.GetPosition()[1] <= text2.GetPosition()[1]+100 and text4.GetPosition()[1]+30 >= text2.GetPosition()[1])):
					ycollide2 = True
				if xcollide2 == True and ycollide2 == True:
					collision2 = True
				if collision2 == True:   
					print 'Treffer!'
					texture.LoadFromFile(".messer.png")
					texture2.LoadFromFile(".stickmanBlood.png")
					texture3.LoadFromFile(".Blood.png")
					texture4.LoadFromFile('.tuxBlood.png')
			#texture4.LoadFromFile('.messer2Blood.png')
			text4.SetPosition(random.randint(0,770),random.randint(0,570))
			
		else:
			print event.Type
			
		if ((weapon.GetPosition()[0]+30 >= text2.GetPosition()[0] and weapon.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (weapon.GetPosition()[0] <= text2.GetPosition()[0]+50 and weapon.GetPosition()[0] >= text2.GetPosition()[0])) or (((weapon.GetPosition()[1]+30 >= text2.GetPosition()[1] and weapon.GetPosition()[1] <= text2.GetPosition()[1]+100) or (weapon.GetPosition()[1] <= text2.GetPosition()[1]+100 and weapon.GetPosition()[1]+30 >= text2.GetPosition()[1]))):
			if (weapon.GetPosition()[0]+30 >= text2.GetPosition()[0] and weapon.GetPosition()[0]+30 <= text2.GetPosition()[0]+50) or (weapon.GetPosition()[0] <= text2.GetPosition()[0]+50 and weapon.GetPosition()[0] >= text2.GetPosition()[0]):
				xcollide = True			
			if ((weapon.GetPosition()[1]+30 >= text2.GetPosition()[1] and weapon.GetPosition()[1] <= text2.GetPosition()[1]+100) or (weapon.GetPosition()[1] <= text2.GetPosition()[1]+100 and weapon.GetPosition()[1]+30 >= text2.GetPosition()[1])):
				ycollide = True
			if xcollide == True and ycollide == True:
				collision = True
				if collision == True:
					print 'Treffer!'
					texture.LoadFromFile(".messerBlood.png")
					texture2.LoadFromFile(".stickmanBlood.png")
					texture3.LoadFromFile(".Blood.png")
					text3.SetPosition(random.randint(-10,10)+text2.GetPosition()[0],random.randint(-10,30)+text2.GetPosition()[1]) 
    # Draw the text, and update the window
    window.Clear(sf.Color.Blue)
    window.Draw(weapon)
    window.Draw(text2)
    window.Draw(text3)
    window.Draw(text4)
    window.Draw(fps)
    window.Display()
# Anstatt nur bei Knopfdruck die Position des Tux random zu setzen soll sie nach einer bestimmten Zeit erneuert werden.
# Wenn ich mit dem Messer auf den Tux gehe und die linke Maustaste druecke soll das Fenstergeschlossen werden und ein neues Programm geoeffnet werden.
# Windows Logo abstechen bringt Punkte


