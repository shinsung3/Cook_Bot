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
driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')

keywords =[]
links = []

FindUrl = "http://www.10000recipe.com"

links2 = []

# 오늘의 레시피 랭킹
def crawl_detail_recipe1(text, driver):

    url = "http://www.10000recipe.com/ranking/list.html?type=hot"
    options = []
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')
    driver.get(url)
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")


    keywords = []
    line = 1
    today = soup.find_all("div", class_="today_caption")
    today = re.compile("    (\S+.*?)    ").findall(str(today))

    driver.quit()
    a = soup.find_all("div", class_="ranking_today")
    s = re.compile(r'href="([a-z0-9/]+)"')
    links = s.findall(str(a))

    for x in links:
       links2.append(FindUrl + x)

    # 하이퍼링크를 찾아오는것
    for y in soup.find_all("div", class_="ranking_today"):
       links.append(FindUrl + y.find("a")["href"])
    print(links)

    # 오늘의 레시피 랭킹 크롤링 (제목)
    for i in today:
       keywords.append("<" + links2[line-1]+ "|" + str(line) + "위 " + i.strip().replace("\n", ' ') + ">\n")
       line += 1

    return "오늘의 인기 레시피 순위! Top 10!!\n" + u'\n'.join(keywords)