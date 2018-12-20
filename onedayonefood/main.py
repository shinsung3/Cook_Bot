# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from recipeSearchKeyword import *

from bs4 import BeautifulSoup
from slackclient import SlackClient
from selenium import webdriver
from flask import Flask, request, make_response, render_template


app = Flask(__name__)

slack_token = "xoxb-502761537154-508511707139-YvPdap9lRvMqbGZSqNqu3uq8"
slack_client_id = "502761537154.510016672070"
slack_client_secret = "cd625f3ca20cd0d50cf83c2566587a10"
slack_verification = "cd625f3ca20cd0d50cf83c2566587a10"
sc = SlackClient(slack_token)
driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')
# http://cc01b936.ngrok.io/listening

# 사용자 호출 전에 실행되어야 할 것
# new_ = []
# 크롤링 함수 구현하기

def _crawl_naver_keywords(text):
    FindUrl = "http://www.10000recipe.com"
    a = "http://www.10000recipe.com/recipe/list.html?q=&cat1=&cat2=&cat3="
    b = "&cat4=&order=accuracy&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource="
    new_ = []
    new = []
    line = 1
    links = []
    # links_ = []
    # i = 0
    keywords = []
    if "소고기" in text:
        key = 70
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")

        for y in soup.find_all("div", class_="col-xs-4"):
            links.append(FindUrl + y.find("a")["href"])
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
            new_.append(x.get_text())
            line += 1
        print(links)
        # print(keywords)
        # for y in soup.find_all("div", class_="col-xs-4"):
        #     links.append(FindUrl + y.find("a")["href"])
        #
        # for z in links:
        #     keywords.append(
        #         "<" + links[i] + "|" + str(i + 1) + "위: " + products[i].get_text().strip().replace('\n', ' ') + ">\n")
        # keywords.append(

    elif "돼지고기" in text:
        key = 71
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):

            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", "").replace('♡',''))
            new_.append(x.get_text())
            line += 1
    elif "닭고기" in text:
        key = 72
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "육류" in text:
        key = 23
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "채소류" in text:
        key = 28
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "해물류" in text:
        key = 24
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "달걀" in text:
        key = 50
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", "").replace("☆",""))
            new_.append(x.get_text())
            line += 1
    elif "유제품" in text:
        key = 50
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", "").replace("☆", ""))
            new_.append(x.get_text())
            line += 1
    elif "가공식품류" in text:
        key = 33
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "쌀" in text:
        key = 47
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "밀가루" in text:
        key = 32
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "건어물" in text:
        key = 25
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "버섯" in text:
        key = 31
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            # line += 1
    elif "과일" in text:
        key = 48
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "콩" in text:
        key = 27
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "견과류" in text:
        key = 27
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "곡류" in text:
        key = 26
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif "기타"in text:
        key = 34
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    elif  "아무거나"  in text:
        key = 34
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            new.append(str(line) + "번 " + x.get_text().replace("\n", ' ').replace("★", ""))
            new_.append(x.get_text())
            line += 1
    else:
        # driver.get("http://www.10000recipe.com/recipe/list.html")
        # searchText = driver.find_element_by_id("srhRecipeText")
        # searchText.send_keys(text)
        # bt = driver.find_element_by_css_selector("button.btn.btn-default")
        # bt.click()
        # new.append(driver.page_source)
        crawl_detail_recipe(text,driver)

    return u'\n'.join(new)

# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        # msg = {}
        # msg['text'] = "Cook Bot!"
        # msg["image_url"] = "http://recipe1.ezmember.co.kr/img/thumb_over.png"
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]
        keywords = _crawl_naver_keywords(text)

        # menus = choice_menu(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords,
            # attachments = json.dumps([msg])
        )


        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is readysssssss</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5223)
