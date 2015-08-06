#/usr/bin/python3.4
# -*- coding: utf-8 -*-
from urllib import request
import gettorrents
import streamtorrent
try:
	from bs4 import BeautifulSoup
except :
	print("Please install beautifulsoup before running this program")

niceTitles = [] 
linkholder = "" 
magnet = [] 
unformatedtitle = []
	global linkholder
	global magnet
	global niceTitles
	global unformatedtitle
	if data == "http://www.cpasbien.pw/":
		req_url = request.urlopen(data).read()
		soup = BeautifulSoup(req_url)
		ha = soup.find_all("a", {"class":"titre"})
		it = ha[0:40]
		for ni in it:
			unformatedtitle.append(ni.get_text())
			nice = ni.get_text().replace(" ","-").replace(":","\b-\b").replace("’","-").replace("(","").replace(")","").replace("&","\b-\b").replace("'","-").lower()
			niceTitles.append(nice)
		for i in range(len(niceTitles)):
			print(i, " = " + niceTitles[i])
		print("What do you wish to do now?")
		print("1: Stream the torrent from list above\n2: Quit")
		userinput = int(input("Enter here: "))
		if userinput == 1:
			print("Enter the index number of movie")
			userinput = int(input())
			lhol = (gettorrents.get(userinput,niceTitles,magnet))
			streamtorrent.stream(lhol)
	elif data == "http://www.cpasbien.pw/view_cat.php?categorie=films":
		def movies(url2):
			req_url = request.urlopen(data).read()
			soup = BeautifulSoup(req_url)
			ha = soup.find_all("a", {"class":"titre"})
			for ni in ha:
				unformatedtitle.append(ni.get_text())
				nice = ni.get_text().replace(" ","-").replace(":","\b-\b").replace("’","-").replace("(","").replace(")","").replace("&","\b-\b").replace("'","-").lower()
				niceTitles.append(nice)
		movies(data)	
		for i in range(len(niceTitles)):
			print(i, " = " + niceTitles[i])
		print("What do you wish to do now?")
		print("1: Stream the torrent from list above\n2: Quit")
		userinput = int(input("Enter here: "))
		if userinput == 1:
			print("Enter the index number of movie")
			userinput = int(input())
			lhol = (gettorrents.get(userinput,niceTitles,magnet))
			streamtorrent.stream(lhol)	
	elif data == "http://www.cpasbien.pw/view_cat.php?categorie=series":
		def series(url2):
			global niceTitles, magnet
			req_url = request.urlopen(data).read()
			soup = BeautifulSoup(req_url)
			ha = soup.find_all("a", {"class":"titre"})
			for ni in ha:
				unformatedtitle.append(ni.get_text())
				nice = ni.get_text().replace(" ","-").replace(":","\b-\b").replace("’","-").replace("(","").replace(")","").replace("&","\b-\b").replace("'","-").lower()
				niceTitles.append(nice)
		series(data)
		for i in range(len(niceTitles)):
			print(i, " = " + niceTitles[i])
		print("What do you wish to do now?")
		print("1: Stream the torrent from list above\n2: Quit")
		userinput = int(input("Enter here: "))
		if userinput == 1:
			print("Enter the index number of movie")
			userinput = int(input())
			lhol = (gettorrents.get(userinput,niceTitles,magnet))
			streamtorrent.stream(lhol)