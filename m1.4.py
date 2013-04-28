#!/usr/bin/env python

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
texture.LoadFromFile(".messer.png")
texture2.LoadFromFile(".stickman2.png")
texture3.LoadFromFile(".BlueBlood.png")
weapon = sf.Sprite(texture)
weapon.Move(150,150)
text2 = sf.Sprite(texture2)
text3 = sf.Sprite(texture3)
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
    collision = False
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
				text3.SetPosition(0,0)
				  
			else:
				print event.Key.Code
				
		elif event.Type == 10:

			print event.MouseMove.X
			x = event.MouseMove.X
			print event.MouseMove.Y
			y = event.MouseMove.Y
			print "----------------"
			weapon.SetPosition(x,y)
			    
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
    window.Draw(fps)
    window.Display()


