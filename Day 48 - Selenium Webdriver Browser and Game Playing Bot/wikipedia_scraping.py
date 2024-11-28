from selenium import webdriver 
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

statistics_number = driver.find_element(By.ID, value="articlecount")
print(statistics_number.text)
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)