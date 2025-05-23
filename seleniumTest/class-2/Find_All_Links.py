import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Open the URL
driver.get("https://parabank.parasoft.com/parabank/")
time.sleep(3)

# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

# Find all links on the page
links = driver.find_elements(By.TAG_NAME, "a")
# Print the text and href attribute of each link
for lk in links:
    print(lk.text, " => ", lk.get_attribute("href"))


driver.quit()