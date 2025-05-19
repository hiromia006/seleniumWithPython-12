import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

print(driver.title)
print(driver.current_url)

st=driver.find_element(By.XPATH, "//div[@class='login_logo']").text
print(st)

driver.quit()