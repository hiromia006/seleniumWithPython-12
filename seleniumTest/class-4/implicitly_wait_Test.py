import time

from selenium import webdriver

driver=webdriver.Chrome()
# Open the URL
driver.get("https://demoqa.com/alerts")
# Maximize the window
driver.maximize_window()

# Implicitly wait for elements to be present
driver.implicitly_wait(10)

# Click on the first alert button
driver.find_element("id", "alertButton").click()
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)

# Click on the second alert button
driver.find_element("id", "confirmButton").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)

# Click on the third alert button
driver.find_element("id", "promtButton").click()
time.sleep(3)
al = driver.switch_to.alert
al.send_keys("Hello, this is a test message!")
time.sleep(2)
print(al.text)
al.accept()
time.sleep(2)

driver.quit()