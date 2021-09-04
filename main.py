#connection a la voie serie
import serial 
import os, sys
import re
import time
from releve import premier
from releve import deuxieme
from releve import brbr

while 1:
	ser = serial.Serial('COM7', 9600)
	i = 1
	linedef = ""
	line = ""
	line = ser.readline()
	line = str(line)
	linedef = linedef + line
	line = ser.readline()
	line = str(line)
	linedef = linedef + line
	line = linedef
	i = 0
	a = 1
	fini = ""
	liste = []
	for letter in line:
		if ((i != 0) and (i != 1) and (i != 30) and (i != 31) and (i != 32) and (i != 33) and (i != 34) and (i != 35) and (i != 36) and (i != 76) and (i != 77) and (i != 78) and (i != 79) and (i != 80) and (i != 81)):
			liste.extend([letter])
		i += 1
	liste.insert(28, ".")
	liste.insert(29, " ")
	liste.pop()
	liste.pop()
	liste.pop()
	liste.pop()
	listedef = "".join(liste)
	listedef = listedef + "l'air."
	heure = str(time.ctime())

	doc = os.open("meteo.html", 1)
	ecrit = str(premier + heure + brbr + str(listedef) + deuxieme).encode("utf-8")
	os.write(doc, bytes(ecrit))


	#Connection au serveur ftp
	from ftplib import FTP
	host = "ftp.lescigales.org" 
	user = "s61_ftp "
	password = "1HJu4hdD" 
	connect = FTP(host,user,password) 
	f_name = "meteo.html"
	f = open(f_name, 'rb')
	connect.storbinary('STOR ' + f_name, f)
	connect.close()
	time.sleep(360)