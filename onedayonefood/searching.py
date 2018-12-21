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

FindUrl = "http://www.10000recipe.com"
keywords = []

def crawl_detail_recipe(text, driver):
    #  open website?
    options = []
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    # driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')
    driver.get("http://www.10000recipe.com/recipe/list.html")
    # 검색창에 검색
    search_text = driver.find_element_by_id("srhRecipeText")
    text = re.sub(r'<@\S+> ', '', text)

    search_text.send_keys(text)  # text

    search_btn = driver.find_element_by_css_selector("button.btn.btn-default")
    search_btn.click()

    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")
    driver.quit()
    menu = soup.find_all("h4", class_="ellipsis_title2")

    link = []
    line = 1
    # 하이퍼링크를 찾아오는 것
    for y in soup.find_all("div", class_="col-xs-4"):
       link.append(FindUrl + y.find("a")["href"])

    # print(links)
    for i in menu:
       # 하이퍼링크 달아주는 부분 + 순서
       keywords.append("<" + link[line - 1] + "|" + str(line) + "번 " + i.get_text().strip().replace("\n", ' ') + ">\n")
       line += 1
    print(keywords)


    return text + "(으)로 만들수 있는 레시피 추천★ \n" + u'\n'.join(keywords)

# def _search_eh_(event_type, slack_event, sc, text2):
#     print(slack_event["event"])
#
#     if event_type == "app_mention":
#         msg = {}
#         msg['text'] = text2
#         msg["image_url"] = "http://recipe1.ezmember.co.kr/img/thumb_over.png"
#         # channel = slack_event["event"]["channel"]
#         # text = slack_event["event"]["text"]
#         # keywords = _crawl_naver_keywords(text)
#
#         # menus = choice_menu(text)
#         sc.api_call(
#             "chat.postMessage",
#             # channel=channel,
#             # text=keywords
#             attachments = json.dumps([msg])
#         )
#
#
#         return make_response("App mention message has been sent", 200, )
