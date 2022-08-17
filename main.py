from bs4 import BeautifulSoup
import requests
import validators

def getpage():
    page_request = input('what do you want to search? : ').replace(" ", "_") # lk_append = page_request.replace(" ", "_") #replaces spaces with underscores
    if validators.url(page_request):
        return page_request
    else: 
        print('That page does not exist. Try something else')
        exit()


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




    

