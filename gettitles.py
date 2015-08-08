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
def get(data):
	global linkholder
	global magnet
	global niceTitles
	global unformatedtitle
	def get_size(url):
		if url == "http://www.cpasbien.pw":
			req = request.urlopen(url).read()
			soup = BeautifulSoup(req)
			gsize = soup.find_all("div",{"class":"poid"})
			gsize = gsize[0:40]
			size = []
			for i in range(len(gsize)):
				size.append(gsize[i])
			return size
		else:
			req = request.urlopen(url).read()
			soup = BeautifulSoup(req)
			gsize = soup.find_all("div",{"class":"poid"})
			size = []
			for i in range(len(gsize)):
				size.append(gsize[i])
			return size
		
	if data == "http://www.cpasbien.pw/":
		req_url = request.urlopen(data).read()
		soup = BeautifulSoup(req_url)
		ha = soup.find_all("a", {"class":"titre"})
		it = ha[0:40]
		for ni in it:
			unformatedtitle.append(ni.get_text())
			nice = ni.get_text().replace(" ","-").replace(":","\b-\b").replace("’","-").replace("(","").replace(")","").replace("&","\b-\b").replace("'","-").lower()
			niceTitles.append(nice)
		size = get_size(data)
		print("#"*50)
		for i in range(len(niceTitles)):
<<<<<<< HEAD
			print(i, " = " + unformatedtitle[i] +" size = "+ str(size[i])[18:-7])
		print("#"*50)
=======
			print(i, " = " + niceTitles[i])
>>>>>>> c59690854b22913c0badf8e59f61045033ca2714
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
		size = get_size(data)
		movies(data)	
		for i in range(len(niceTitles)):
<<<<<<< HEAD
			print(i, " = " + unformatedtitle[i] +" size = "+ str(size[i])[18:-7])
=======
			print(i, " = " + niceTitles[i])
>>>>>>> c59690854b22913c0badf8e59f61045033ca2714
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
		size = get_size(data)
		series(data)
		for i in range(len(niceTitles)):
<<<<<<< HEAD
			print(i, " = " + unformatedtitle[i] +" size = "+ str(size[i])[18:-7])
=======
			print(i, " = " + niceTitles[i])
>>>>>>> c59690854b22913c0badf8e59f61045033ca2714
		print("What do you wish to do now?")
		print("1: Stream the torrent from list above\n2: Quit")
		userinput = int(input("Enter here: "))
		if userinput == 1:
			print("Enter the index number of movie")
			userinput = int(input())
			lhol = (gettorrents.get(userinput,niceTitles,magnet))
			streamtorrent.stream(lhol)