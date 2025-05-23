import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Open the URL
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)

# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

el = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
print("Color: ", el.value_of_css_property("color"))
print("Font Size: ", el.value_of_css_property("font-size"))
print("Font Family: ", el.value_of_css_property("font-family"))
print("Font Weight: ", el.value_of_css_property("font-weight"))

driver.get("https://parabank.parasoft.com/parabank/")
time.sleep(3)
#at = driver.find_element(By.NAME, "username").get_attribute("class")
print("Attribute: ", driver.find_element(By.NAME, "username").get_attribute("class"))

driver.quit()
