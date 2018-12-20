# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template
from selenium import webdriver

app = Flask(__name__)

slack_token = "xoxb-507694811781-508898931990-Dc2QfyVKbON8rjiQNsmeG3wf"
slack_client_id = "507694811781.507391404675"
slack_client_secret = "98c92f641eacb8a7a451aafd755586ab"
slack_verification = "b3wEFULIODSrJr6WY3MVkW6x"
sc = SlackClient(slack_token)

driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')


# 세부 레시피 크롤링
def crawl_detail_recipe(text):
    #  open website
    driver.get("http://www.10000recipe.com/recipe/list.html")
    # 검색창에 검색
    search_text = driver.find_element_by_id("srhRecipeText")
    text = re.sub(r'<@\S+> ', '', text)

    search_text.send_keys(text)  # text

    search_btn = driver.find_element_by_css_selector("button.btn.btn-default")
    search_btn.click()

    bt = driver.find_element_by_class_name("thumbnail")
    bt.click()

    # 엘리스 url
    # url = "http://www.10000recipe.com/recipe/6853017"
    # source = urllib.request.urlopen(url).read()
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")

    contents = soup.find("div", class_="view_step")
    contents.find("script")
    if contents.find("script"):
        contents.find("script").extract()
    contents = contents.get_text().strip()

    return contents


# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):
    print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        keywords = crawl_detail_recipe(text)
        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
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
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
