import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# Open the URL
driver.get("https://www.saucedemo.com/")
#time.sleep(4)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)


driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
#time.sleep(4)

driver.find_element(By.ID, "login-button").click()
#time.sleep(4)
driver.find_element(By.ID, "react-burger-menu-btn").click()
#time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(3)
driver.quit()