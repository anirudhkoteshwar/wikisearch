from bs4 import BeautifulSoup
import requests
# import validators         # validators wasnt working as intended

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

asciiart()
html_content = getpage()
page = requests.get(f"https://en.wikipedia.org/wiki/{html_content}").text # get the webpage from wikipedia
soup = BeautifulSoup(str(page), 'lxml') # input the content to beautiful soup

titletag = soup.find('h1') # find the title of the webpage
title = titletag.text # get the text in that tag
sections = soup.find_all('span', class_='mw-headline') #find all the headings h2
paras = soup.find_all('p') #find all paragraphs

print(title)
for head in sections:
    print(head.text)




    

