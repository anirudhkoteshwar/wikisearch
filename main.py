from bs4 import BeautifulSoup
import requests

page_request = input('what do you want to search? : ')
page = requests.get(f"https://en.wikipedia.org/wiki/{page_request}").text # get the webpage from wikipedia
soup = BeautifulSoup(str(page), 'lxml') # input the content to beautiful soup

titletag = soup.find('h1') # find the title of the webpage
title = titletag.text # get the text in that tag
sections = soup.find_all('span', class_='mw-headline') #find all the headings h2
paras = soup.find_all('p')

print(title)
for head in sections:
    print(head.text)




    

