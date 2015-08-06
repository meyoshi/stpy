#/usr/bin/python3.4
# -*- coding: utf-8 -*-
""""""
def get(data ,nicetitle , magnet):
	for i in range(len(nicetitle)):
		magnet.append("http://www.cpasbien.pw/telechargement/"+nicetitle[i]+".torrent")
	linkholder =  magnet[data]
	return linkholder