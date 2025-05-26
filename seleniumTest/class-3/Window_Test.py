import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# Open the URL
driver.get("https://demoqa.com/browser-windows")
time.sleep(4)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

windStr=driver.current_window_handle
print("Current Window Handle: ", driver.find_element(By.CSS_SELECTOR, ".text-center").text)

driver.switch_to.new_window("window")
time.sleep(3)
driver.get("https://demoqa.com/sample")
print("New Tab Title: ", driver.title)

print("Tab: ", driver.find_element(By.ID, "sampleHeading").text)
time.sleep(4)
driver.close()
time.sleep(4)
driver.switch_to.window(windStr)

print("Bact to Current Window Handle: ", driver.find_element(By.CSS_SELECTOR, ".text-center").text)

driver.quit()