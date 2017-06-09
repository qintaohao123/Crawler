
import urllib
import urllib2
import re
#coding=UTF-8 
def getImgURLs(html):
reg = r'src=.+/.jpg' # Is the reg right?
imgReg = reg.compile(reg)
imglist = imgReg.Findall(html)


def saveImgs(imgURLlist, name):



html = getHtml("http://tieba.baidu.com/p/4939865204")	
dd