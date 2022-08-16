from bs4 import BeautifulSoup

with open('apple.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    paragraphs = soup.find_all('h2')
    for x in paragraphs:
        print(x.text)

