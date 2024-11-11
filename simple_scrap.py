#       This is my project related to auto webscraping

import requests
from bs4 import BeautifulSoup

# Replace 'URL' with the URL of the page you want to scrape
url = 'https://en.wikipedia.org/wiki/Generative_artificial_intelligence'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title (usually within the <h1> tag)
    title = soup.find('h1').get_text() if soup.find('h1') else 'No Title Found'
    print(f'Title: {title}')

    # Extract all paragraphs within <p> tags
    paragraphs = soup.find_all('p')
    content = ' '.join([para.get_text() for para in paragraphs])
    print(f'Content: {content}')
else:
    print("Failed to retrieve the page")




#<<<<<<<<<<<<<<-----Under develpment------------>>>>>>>>>>>>>>>>>