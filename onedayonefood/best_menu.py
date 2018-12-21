import json
import os
import re
import time
import urllib.request

from recipeSearchKeyword import *

from bs4 import BeautifulSoup
from slackclient import SlackClient
from selenium import webdriver
from flask import Flask, request, make_response, render_template

new = []
links = []
links2 = []
FindUrl = "http://www.10000recipe.com"

def best_menu(text):
    now = time.localtime()
    s = "%04d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday)
    print(s)
    url = "http://www.10000recipe.com/ranking/list.html?type=hot&ymd=" + str(s)
    print(url)
    line = 1
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    y = soup.find_all("div", class_="ranking_today")
    s = re.compile(r'href="([a-z0-9/]+)"')
    links = s.findall(str(y))
    for x in links:
        links2.append(FindUrl + x)
    print(links2)
    for x in soup.find_all("span", class_="today_pic"):

        new.append("<" + links2[line-1] + "|" + str(line) + "위 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
        line += 1
    print(new)
    a = soup.find("span", class_="top_icon").get_text().strip()
    return "★" + "가장 인기가 많은 요리 블로거" + "★\n" + u'\n'.join(new)