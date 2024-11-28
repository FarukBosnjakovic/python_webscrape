# How to automate filling out forms and Clicking Buttons

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find element by CSS SELECTOR
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)

# Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)