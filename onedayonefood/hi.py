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
FindUrl = "http://tv.jtbc.joins.com/photo/pr10010331/pm10026814/detail/"

def hi(text):
    url = "http://tv.jtbc.joins.com/photo/pr10010331/pm10026814"
    # print(url)
    line = 1
    source = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(source, "html.parser")
    # print(soup)
    y = soup.find_all("ul", class_="clfix")
    s = re.compile(r'href="http://tv.jtbc.joins.com/photo/pr10010331/pm10026814/detail/([0-9]+)"')
    links = s.findall(str(y))
    print(links)
    for x in links:
        links2.append(FindUrl + x)
    print(links2)
    for x in soup.find_all("span", class_="txt"):
        new.append("<" + links2[line-1] + "|" + str(line) + "위 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
        line += 1
    print(new)
    # a = soup.find("span", class_="top_icon").get_text().strip()
    return "★" + "냉부 쉐프들의 요리 추천!" + "★\n" + u'\n'.join(new)