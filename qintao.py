

import urllib.request
import re
import os
#coding=UTF-8 
#

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html


def getImgURLs(html,reg):
	print (html)
	imgReg = re.compile(reg)
	imglist = re.findall(imgReg,repr(html))
	return imglist


def saveImgs(imgURLslist, fileDir):
	#creat directory of files
	#
	
	if not (os.path.exists(fileDir)):
		os.makedirs(fileDir)
	
	#get images from imageurlsList
	x=0
	for imgurl in imgURLsList:
		 
		workPath=os.path.join(fileDir,'%02d.jpg'%x)  
		urllib.request.urlretrieve(imgurl,workPath)
		x+=1

	print ('x is %s',x)

reg = r'http://[\S]*\.jpg' # Is the reg right?
html = getHtml("http://tieba.baidu.com/p/4939865204")	
imgURLsList = getImgURLs(html,reg)
imgsDir = 'E:/qintao'

saveImgs(imgURLsList,imgsDir)


