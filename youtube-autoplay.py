#!usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import urllib
from bs4 import BeautifulSoup
import sys

arg = len(sys.argv)

search = ""
display = ""
for x in range(1, arg):
    search += sys.argv[x]
    display += sys.argv[x]
    if (x == arg-1):
        break
    search += "+"

print "\n Now Playing " + display
browser = webdriver.Chrome("C:\Program Files\chromedriver_win32\chromedriver")


url = "https://www.youtube.com/results?search_query=" 
url += search
browser.get(url)

time.sleep(1)

url = browser.current_url
request = urllib.urlopen(url).read()
soup = BeautifulSoup(request,"html.parser") #extract html content inside tags.
searchdiv = soup.find_all("div", class_="yt-lockup-dismissable yt-uix-tile") #This is the div class of the search results in YouTube


prefix = "http://youtube.com"
prefix = prefix + searchdiv[0].a["href"] #Get the url of the first search result
browser.get(prefix)
