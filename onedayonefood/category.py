# import json
# import os
# import re
# import time
# import urllib.request
#
# from data_cook import key_for_food
# from main_keyword import *
#
# from recipeSearchKeyword import *
#
# from bs4 import BeautifulSoup
# from slackclient import SlackClient
# from selenium import webdriver
# from flask import Flask, request, make_response, render_template
#
# def _crawl_naver_keywords(text):
#     text2 = re.sub('<@\S+> ', '', text)
#     FindUrl = "http://www.10000recipe.com"
#     a = "http://www.10000recipe.com/recipe/list.html?q=&cat1=&cat2=&cat3="
#     b = "&cat4=&order=accuracy&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource="
#     # new_ = []
#     new = []  # 결과 출력 리스트
#     line = 1  # 순위, 순번을 나타내는 line
#     links = []  # 하이퍼링크 추출 후 저장 리스트
#     indgre_key = main_keyword(text)
#
#     if indgre_key:
#         url = a + str(indgre_key) + b
#         source = urllib.request.urlopen(url).read()
#         soup = BeautifulSoup(source, "html.parser")
#
#         # 하이퍼링크를 찾아오는 것
#         for y in soup.find_all("div", class_="col-xs-4"):
#             links.append(FindUrl + y.find("a")["href"])
#         for x in soup.find_all("h4", class_="ellipsis_title2"):
#             # 하이퍼링크 달아주는 부분 + 순서
#             new.append(
#                 "<" + links[line - 1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace(
#                     "★", "") + ">\n")
#             line += 1
#
#         # print(links)
#         # 제목 다는 부분
#         return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)