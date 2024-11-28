from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

# Keep Firefox (Chrome) browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Firefox()
# driver.get("https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_2?crid=1DWI960WFFBQT&dib=eyJ2IjoiMSJ9.2M_JmHUuuGWqoDmI6lJd5OEvJvf-3I8Z42YMhv_ut04HRc7f06SqsjyFKG_q-Lv-UN_8sT6aMZZIqcnKtRAV4rjhSHzIt_SdaA1lHML79b-thG20SaebTdBJwk4PirgthQM0LNt_fqPkjMVdsYfzDRKlERdBzNiEYex4uIXilaBXFvJcJLcYolK_t8bZAZQR85CS7YchcwHTfOOaUwg9FEarehL1YKEtSMdKSG8ovfE.RT3GJq3I9hk8IX8Y0WYqy2s3rdiJSPnuEEvPlo-0Qng&dib_tag=se&keywords=instant%2Bpot&qid=1705871452&sprefix=instant%2Caps%2C203&sr=8-2&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f'Price is {price_dollar.text}.{price_cents.text}')

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q") 
# print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.ID, value="submit")
print(button.size)
docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(docs_link.text)

print()

# XPath Example
bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
print(bug_link.text)

print()

# Find elements (method returns a list)


# driver.close() # zatvori tab
# driver.quit() # zatvori program