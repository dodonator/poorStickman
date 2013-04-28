from PySFML import *
import time
import os
import datetime
import getpass
import random
os.system('clear')

fontSize = 30

# Create the main window
window = sf.RenderWindow(sf.VideoMode(900, 600), "THE MENU HAS YOU!")
menuTitle = sf.String('Waehle ein Spiel:')
menuTitle.SetPosition(70, 70)
menuTitle.SetColor(sf.Color.Red)

menueTexts = []
menueTexts.append('m1 Toete mit einem Messer deinen Stickman!')
menueTexts.append('m2 Die Abrechnung mit einem bekannten italienischen Klempner')
menueTexts.append('m3 Die Wahrheit')
menueTexts.append('m4 JoystickFoo auf Basis von m1')
menueTexts.append('m0 Der Ausgangspunkt von m1, m2 und m3!')
menueTexts.append('O  Ein Spiel auf Basis von m1 mit OTP')



menuItems = []
yCounter = 0
for menText in menueTexts:
	tmp = sf.String(menText)
	tmp.SetPosition(30,100 + (yCounter * (fontSize)))
	tmp.SetSize(fontSize)
	menuItems.append(tmp)
	yCounter += 1


def drawList(window, listToDraw):
	for drawable in listToDraw:
		window.Draw(drawable)


def reselectMenuItem(menuItems, menueTexts, selectedMenuItem, direction):
	reselectedItem = (selectedMenuItem + direction)
	print 'selectedMenuItem', reselectedItem
	if reselectedItem < 0:
		reselectedItem = len(menueTexts) -1
	elif reselectedItem > len(menueTexts) -1:
		reselectedItem = 0
	
	for i in range(0,len(menueTexts)):
		if i == reselectedItem:
			menuItems[i].SetText('>' + menueTexts[i] + '<')
		else:
			menuItems[i].SetText(menueTexts[i])
	print 'selectedMenuItem', reselectedItem
	return reselectedItem

selectedMenuItem = 0
running = True
window.ShowMouseCursor(False)
reselectMenuItem(menuItems, menueTexts, selectedMenuItem, 0)
while running:
	event = sf.Event() 
	xcollide = False
	ycollide = False
	collision = False
	while window.GetEvent(event):
		if event.Type == sf.Event.Closed:
			running = False
		elif event.Type == sf.Event.KeyPressed:
			if event.Key.Code == 278: # enter
				running = False
			elif event.Key.Code == 293: #up
				#selectedMenuItem -= 1
				selectedMenuItem = reselectMenuItem(menuItems, menueTexts, selectedMenuItem, -1)
			elif event.Key.Code == 294: #down
				#selectedMenuItem += 1
				selectedMenuItem = reselectMenuItem(menuItems, menueTexts, selectedMenuItem, 1)
			else:
				print event.Key.Code
				
	# Draw the text, and update the window
	window.Clear(sf.Color.Black)
	window.Draw(menuTitle)
	drawList(window, menuItems)
	
	window.Display()
	
if selectedMenuItem == 0:
	os.system('python m1.4.py')
	
elif selectedMenuItem == 1:
	os.system('python m2.10.py')
	
elif selectedMenuItem == 2:
	os.system('python m3.14.py')
	
elif selectedMenuItem == 3:
	os.system('python m4.py')
	
elif selectedMenuItem == 4:
	os.system('python bladeOriginal.py')
elif selectedMenuItem == 5:
	os.system('python OTP.py')
