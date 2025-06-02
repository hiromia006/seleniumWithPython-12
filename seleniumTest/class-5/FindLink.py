import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.tutorialspoint.com/selenium/practice/links.php")
# Maximize the window
driver.maximize_window()

# Wait for the page to load
driver.implicitly_wait(10)

alist = driver.find_elements(By.TAG_NAME, "a")
# Print the text and href attribute of each link
for lk in alist:
    print(lk.text, " => ", lk.get_attribute("href"))

driver.quit()