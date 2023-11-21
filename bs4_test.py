import requests
from bs4 import BeautifulSoup

URL = "https://www.instagram.com/explore/tags/naturabroficial/"

# URL = 'https://www.estadao.com.br/'

page = requests.get(URL)


# print(soup)

soup = BeautifulSoup(page, 'html.parser')
links_with_text = []
for a in soup.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])