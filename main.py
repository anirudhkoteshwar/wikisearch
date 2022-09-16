"""
    Wikisearch
    Anirudh Koteshwar
    12-8-2022
"""
from bs4 import BeautifulSoup
import requests

def getpage():
    page_request = input('what do you want to search? : ').replace(" ", "_")
    return page_request

def extractpage(content):
    page = requests.get(f"https://en.wikipedia.org/wiki/{content}").text # get the webpage from wikipedia
    soup = BeautifulSoup(str(page), 'lxml') # input the content to beautiful soup
    title = soup.find('h1') # find the title of the webpage
    #sections = soup.find_all('span', class_='mw-headline') #find all the headings h2
    sections = soup.find_all('h2')
    paras = soup.find_all('p') #find all paragraphs
    return title, sections, paras, soup

html_content = getpage()
title, sections, paras, soup = extractpage(html_content)

heads = {}
i = 1
print(title.text)
for head in sections:
    heads.update({i : head.text})
    i = i + 1

for key,value in heads.items():
    print(key,value)

j = input('Which topic do you want to read? : ')
# print(heads.get(int(j)))
out = soup.find('span',class_='mw-headline', string="%s" % heads.get(int(j)))
print(out.string)
for x in out.children:
    print(x)

    

