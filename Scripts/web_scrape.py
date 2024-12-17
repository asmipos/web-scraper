from bs4 import BeautifulSoup
import requests
response = requests.get('https://www.example.com')
content = response.text
status_code = response.status_code
headers  = response.headers

soup = BeautifulSoup(content, 'html.parser')
print(soup)
print("///////printing html parts//////")
title = soup.select_one('h1').text 
text = soup.select_one('p').text
link = soup.select_one('a').get('href')

print(title)
print(text)
print(link)
