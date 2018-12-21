import json
import os
import re
import time
import urllib.request

from data_cook import key_for_food


from recipeSearchKeyword import *

from bs4 import BeautifulSoup
from slackclient import SlackClient
from selenium import webdriver
from flask import Flask, request, make_response, render_template


def main_keyword(text):


    # key_for_food = {"소고기": 70, "돼지고기": 71, "닭고기": 72, "육류": 23}
    # 음식 데이터를 text로 가져옴
    for i in key_for_food.keys():
        if i in text:
            key = key_for_food[i] #keys
            return key
        else:
            key = -100
            return key
    #
    # if "소고기" in text:
    #     key = 70
    # elif "돼지고기" in text:

