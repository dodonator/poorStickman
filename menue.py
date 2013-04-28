# Dies ist das Steuerungsmenue
import os
os.system('clear')
auswahl = ''
while auswahl != 'q':
	os.system('clear')
	print 'Waehle bitte ein Spiel: '
	print '0: m1 Toete mit einem Messer deinen Stickman!'
	print '1: m2 Die Abrechnung mit einem bekannten italienischen Klempner'
	print '2: m3 Die Wahrheit'
	print '3: m0 Der Ausgangspunkt von m1, m2 und m3!'
	print 'q: Beenden'
	auswahl = raw_input('Entscheide dich!\n')
	if auswahl == '0':
		
		os.system('python m1.3.py')
		
	elif auswahl == '1':
		
		os.system('python m2.9.py')
		
	elif auswahl == '2':
		
		os.system('python m3.11.py')
		
	elif auswahl == '3':
		
		os.system('python bladeOriginal.py')
		
print 'Good Bye'
print ''
