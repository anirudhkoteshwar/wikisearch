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

def asciiart():
    print("""  
     __     __     __     __  __     __     ______     ______     ______     ______     ______     __  __    
    /\ \  _ \ \   /\ \   /\ \/ /    /\ \   /\  ___\   /\  ___\   /\  __ \   /\  == \   /\  ___\   /\ \_\ \   
    \ \ \/ ".\ \  \ \ \  \ \  _"-.  \ \ \  \ \___  \  \ \  __\   \ \  __ \  \ \  __<   \ \ \____  \ \  __ \  
     \ \__/".~\_\  \ \_\  \ \_\ \_\  \ \_\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
      \/_/   \/_/   \/_/   \/_/\/_/   \/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/   \/_____/   \/_/\/_/                                                                                                        
    """)

def extractpage(content):
    page = requests.get(f"https://en.wikipedia.org/wiki/{content}").text # get the webpage from wikipedia
    soup = BeautifulSoup(str(page), 'lxml') # input the content to beautiful soup
    
    title = soup.find('h1') # find the title of the webpage
    sections = soup.find_all('span', class_='mw-headline') #find all the headings h2
    paras = soup.find_all('p') #find all paragraphs
    return title, sections, paras

asciiart()
html_content = getpage()
title, sections, paras = extractpage(html_content)
print(title.text)
for header in sections:
    print(header.text)
for block in paras:
    print(block.text)



    

