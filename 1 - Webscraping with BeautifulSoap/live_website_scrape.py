# SCRAPING A LIVE WEBSITE

from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text 

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.title)
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = [] 

for article_tag in articles:
    text = article_tag.getText() 
    article_texts.append(text)
    link = article_tag.get('href') 
    article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# largest_number = max(article_upvotes) 
# largest_index = article_upvotes.index(largest_number) 

# print(article_texts[largest_index])
# print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)