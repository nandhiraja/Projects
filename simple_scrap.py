#       This is my project related to auto webscraping

import requests
from bs4 import BeautifulSoup


url = 'https://en.wikipedia.org/wiki/Generative_artificial_intelligence'

#  request to the URL
response = requests.get(url)

if response.status_code == 200:
  
    soup = BeautifulSoup(response.content, 'html.parser')


    title = soup.find('h1').get_text() if soup.find('h1') else 'No Title Found'
    print(f'Title: {title}')

    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])
    
    print(f'Content: {content}')
else:
    print("Failed to retrieve the page")




#<<<<<<<<<<<<<<-----Under develpment------------>>>>>>>>>>>>>>>>>