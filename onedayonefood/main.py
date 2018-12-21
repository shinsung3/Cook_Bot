# -*- coding: utf-8 -*-
import json
import os
import re
import time
import urllib.request

from recipeSearchKeyword import *
from best_menu import *
from hi import *
from dongheedong import *
from searching import *
from main_keyword import *


from bs4 import BeautifulSoup
from slackclient import SlackClient
from selenium import webdriver
from flask import Flask, request, make_response, render_template


app = Flask(__name__)


driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')
# http://cc01b936.ngrok.io/listening

# 사용자 호출 전에 실행되어야 할 것
# new_ = []
# 크롤링 함수 구현하기
time1 = ""

def _crawl_naver_keywords(text):
    text2 = re.sub('<@\S+> ','', text)
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
    main_keyword(text)
    if "소고기" in text2:
        key = 70
        url = a + str(key) + b
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")

        #하이퍼링크를 찾아오는 것
        for y in soup.find_all("div", class_="col-xs-4"):
            links.append(FindUrl + y.find("a")["href"])
        for x in soup.find_all("h4", class_="ellipsis_title2"):
            #하이퍼링크 달아주는 부분 + 순서
            new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
            line += 1

        print(links)
        #제목 다는 부분
        return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
        # print(keywords)
        # for y in soup.find_all("div", class_="col-xs-4"):
        #     links.append(FindUrl + y.find("a")["href"])
        #
        # for z in links:
        #     keywords.append(
        #         "<" + links[i] + "|" + str(i + 1) + "위: " + products[i].get_text().strip().replace('\n', ' ') + ">\n")
        # keywords.append(
    #
    # elif "돼지고기" in text2:
    #     key = 71
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "").replace('♡','')+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "닭고기" in text2:
    #     key = 72
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "육류" in text2:
    #     key = 23
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "채소류" in text2:
    #     key = 28
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "해물류" in text2:
    #     key = 24
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "달걀" in text2:
    #     key = 50
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "유제품" in text2:
    #     key = 50
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "가공식품류" in text2:
    #     key = 33
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "쌀" in text2:
    #     key = 47
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "밀가루" in text2:
    #     key = 32
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "건어물" in text2:
    #     key = 25
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "버섯" in text2:
    #     key = 31
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "과일" in text2:
    #     key = 48
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    #
    # elif "콩" in text2:
    #     key = 27
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "견과류" in text2:
    #     key = 27
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "곡류" in text2:
    #     key = 26
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif "기타"in text2:
    #     key = 34
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    # elif  "아무거나"  in text2:
    #     key = 34
    #     url = a + str(key) + b
    #     source = urllib.request.urlopen(url).read()
    #     soup = BeautifulSoup(source, "html.parser")
    #     for y in soup.find_all("div", class_="col-xs-4"):
    #         links.append(FindUrl + y.find("a")["href"])
    #     for x in soup.find_all("h4", class_="ellipsis_title2"):
    #         new.append("<" + links[line-1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★", "")+">\n")
    #         new_.append(x.get_text())
    #         line += 1
    #
    #     print(links)
    #     return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)
    elif "인기블로거" in text2:
        return best_menu(text2)
    elif "냉부" in text2:
        return hi(text2)
    elif "안녕" in text2:
        answer = "1.재료별 카테고리를 입력하세요\n\n : 소고기, 돼지고기, 닭고기, 육류,\n\n 채소류, 해물류,달걀, 유제품,\n\n 가공식품류, 쌀, 밀가루, 건어물류, 버섯류,\n\n 과일류, 콩, 견과류, 곡류, 기타 \n\n\n\n2. 원하는거 아무거나 입력하세요 \n\n\n\n3. '오늘', '오늘 순위'를 검색하면 오늘의 인기 요리!\n\n\n\n4. '냉장고를 부탁해' 쉐프들의 요리가 궁금하다면!? : '냉부'검색!\n\n\n\n5. 인기요리블로거가 궁금하다면 '인기블로거'검색까지!\n\n\n"

        return answer
    elif "추천" in text2:
        answer = "1.재료별 카테고리를 입력하세요\n\n : 소고기, 돼지고기, 닭고기, 육류,\n\n 채소류, 해물류,달걀, 유제품,\n\n 가공식품류, 쌀, 밀가루, 건어물류, 버섯류,\n\n 과일류, 콩, 견과류, 곡류, 기타 \n\n\n\n2. 원하는거 아무거나 입력하세요 \n\n\n\n3. '오늘', '오늘 순위'를 검색하면 오늘의 인기 요리!\n\n\n\n4. '냉장고를 부탁해' 쉐프들의 요리가 궁금하다면!? : '냉부'검색!\n\n\n\n5. 인기요리블로거가 궁금하다면 '인기블로거'검색까지!\n\n\n"


        return answer
    # elif "" in text2:
    #     answer = "1.재료별 카테고리를 입력하세요\n\n : 소고기, 돼지고기, 닭고기, 육류,\n\n 채소류, 해물류,달걀, 유제품,\n\n 가공식품류, 쌀, 밀가루, 건어물류, 버섯류,\n\n 과일류, 콩, 견과류, 곡류, 기타 \n\n\n\n2. 원하는거 아무거나 입력하세요 \n\n\n\n3. '오늘', '오늘 순위'를 검색하면 오늘의 인기 요리!\n\n\n\n4. '냉장고를 부탁해' 쉐프들의 요리가 궁금하다면!? : '냉부'검색!\n\n\n\n5. 인기요리블로거가 궁금하다면 '인기블로거'검색까지!\n\n\n"
    #
    #
    #     return answer
    elif "오늘" in text2:
        return crawl_detail_recipe1(text2, driver)
    elif "오늘 순위" in text2:
        return crawl_detail_recipe1(text2, driver)

    else:
        # driver.get("http://www.10000recipe.com/recipe/list.html")
        # searchtext2 = driver.find_element_by_id("srhRecipetext2")
        # searchtext2.send_keys(text2)
        # bt = driver.find_element_by_css_selector("button.btn.btn-default")
        # bt.click()
        # new.append(driver.page_source)
        # crawl_detail_recipe(text2, driver)
        return crawl_detail_recipe(text2, driver)
        # return u'\n'.join(new)

# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        # msg = {}
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]
        keywords = _crawl_naver_keywords(text)
        # msg['text'] = text
        # msg["image_url"] = "http://recipe1.ezmember.co.kr/img/thumb_over.png"

        # menus = choice_menu(text)
        # if "오늘"in text:
        #     sc.api_call(
        #     "chat.postMessage",
        #     channel=channel,
        #     text=keywords,
        #     attachments = json.dumps([msg])
        #     )
        # else:
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
            # if "오늘" in text:
            #     attachments = json.dumps([msg])
        )


        return make_response("App mention message has been sent", 200, )

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route("/listening", methods=["GET", "POST"])
def hears():
    global time1
    slack_event = json.loads(request.data)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})
    global time1
    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        if slack_event["event"]["event_ts"] != time1:
            time1 = slack_event["event"]["event_ts"]
            return _event_handler(event_type, slack_event)
        else:
            return make_response("duple", 200,)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is readysssssss</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5222)
