    # elif "아무거나" in text2:
    # key = 34
    # url = a + str(key) + b
    # source = urllib.request.urlopen(url).read()
    # soup = BeautifulSoup(source, "html.parser")
    # for y in soup.find_all("div", class_="col-xs-4"):
    #     links.append(FindUrl + y.find("a")["href"])
    # for x in soup.find_all("h4", class_="ellipsis_title2"):
    #     new.append("<" + links[line - 1] + "|" + str(line) + "번 " + x.get_text().strip().replace("\n", ' ').replace("★",
    #                                                                                                                 "") + ">\n")
    #     new_.append(x.get_text())
    #     line += 1
    #
    # print(links)
    # return text2 + "★메뉴 추천★ \n" + u'\n'.join(new)