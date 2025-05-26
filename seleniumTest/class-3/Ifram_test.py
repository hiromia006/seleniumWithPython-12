import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the URL
driver.get("https://demoqa.com/frames")
time.sleep(3)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(30)

# driver.find_element(By.ID, "input1").send_keys("test1")
# driver.find_element(By.ID, "input2").send_keys("test2")
# driver.find_element()

print(driver.find_element(By.CSS_SELECTOR, ".text-center").text)

driver.switch_to.frame("frame1")
print(driver.find_element(By.ID, "sampleHeading").text)
#print(driver.find_element(By.CSS_SELECTOR, ".text-center").text)
driver.switch_to.default_content()  # Switch back to the main content

print(driver.find_element(By.CSS_SELECTOR, ".text-center").text)

# Switch to the second frame
driver.switch_to.frame("frame2")
print(driver.find_element(By.ID, "sampleHeading").text)
driver.switch_to.default_content()  # Switch back to the main content

print(driver.find_element(By.CSS_SELECTOR, ".text-center").text)

driver.quit()