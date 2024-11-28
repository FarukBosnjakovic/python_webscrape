# Sign Up Form

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()
driver.get("http://secure-retreat-92358.herokuapp.com/")


# First Name Signup
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Admin")

# Last Name Signup
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Adminovic")

# Email Address
email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("admin@admin.com") 

# Sign Up Button 
signup_button = driver.find_element(By.CLASS_NAME, value="btn")
signup_button.send_keys(Keys.ENTER)

# Sign Up Button, 2. nacin
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.send_keys(Keys.ENTER)