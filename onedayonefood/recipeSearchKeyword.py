# # -*- coding: utf-8 -*-
# import json
# import os
# import re
# import urllib.request
#
# from bs4 import BeautifulSoup
# from slackclient import SlackClient
# from flask import Flask, request, make_response, render_template
# from selenium import webdriver
#
#
# # 세부 레시피 크롤링
# def crawl_detail_recipe(text,driver):
#     # driver = webdriver.Chrome(r'C:\Users\student\Desktop\chromedriver.exe')
#     #  open website
#     driver.get("http://www.10000recipe.com/recipe/list.html")
#     # 검색창에 검색
#     search_text = driver.find_element_by_id("srhRecipeText")
#     text = re.sub(r'<@\S+> ', '', text)
#
#     search_text.send_keys(text)  # text
#
#     search_btn = driver.find_element_by_css_selector("button.btn.btn-default")
#     search_btn.click()
#
#     bt = driver.find_element_by_class_name("thumbnail")
#     bt.click()
#     driver.quit()
#     # 엘리스 url
#     # url = "http://www.10000recipe.com/recipe/6853017"
#     # source = urllib.request.urlopen(url).read()
#     source = driver.page_source
#     soup = BeautifulSoup(source, "html.parser")
#
#     contents = soup.find("div", class_="view_step")
#     contents.find("script")
#     if contents.find("script"):
#         contents.find("script").extract()
#     contents = contents.get_text().strip()
#
#     return contents