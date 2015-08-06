#/usr/bin/python3.4
# -*- coding: utf-8 -*-
""""""
import gettitles
def secMenu():
	print("1 = Movies\tor\t 2 = Tv seris")
	userinput2 = int(input())
	if userinput2 == 1:
		url = "http://www.cpasbien.pw/view_cat.php?categorie=films"
		gettitles.get(url)
	elif userinput2 == 2:
		url = "http://www.cpasbien.pw/view_cat.php?categorie=series"
		gettitles.get(url)

def mainMenu():
	print("This program uses cpasbien.pw as sources for pass torrents\n")
	print("what do you want to do?\n1 = list the titles of movies or tv series from home page.\n")
	print("2 = list movies from films tab or list only tv series from series tab.\n")
	print("3 = Search for a movie or tv series\n")
	userinput = int(input())
	if userinput == 1:
		url = "http://www.cpasbien.pw/"
		gettitles.get(url)
	elif userinput == 2:
		secMenu()

mainMenu()