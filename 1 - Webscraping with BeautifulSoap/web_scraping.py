# WEB SCRAPING WITH BEAUTIFUL SOUP

from bs4 import BeautifulSoup
import lxml 

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.name) # gives a name of the tag
# print(soup.title.string)
# print()
# print(soup)
# print(soup.prettify())

# print(soup.a)


all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText()) # only prints text in links
    # print(tag.get("href")) # only prints link

heading = soup.find(name="h1", id="name")
print(heading)
print()


section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print()

company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)
