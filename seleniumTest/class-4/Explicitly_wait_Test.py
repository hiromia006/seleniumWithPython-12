import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
# Open the URL
driver.get("https://demoqa.com/alerts")
# Maximize the window
driver.maximize_window()

# Explicitly wait for elements to be present
wait=WebDriverWait(driver, 20)

# Click on the first alert button
wait.until(EC.element_to_be_clickable(("id", "alertButton"))).click()
wait.until(EC.alert_is_present())
time.sleep(3)
driver.switch_to.alert.accept()
# Click on the second alert button


# Click on the second alert button
driver.find_element("id", "confirmButton").click()
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)


# Click on the third alert button
wait.until(EC.element_to_be_present(("id", "promtButton")))
driver.find_element("id", "promtButton").click()
time.sleep(3)
al = driver.switch_to.alert
al.send_keys("Hello, this is a test message!")
time.sleep(2)
print(al.text)
al.accept()
time.sleep(2)

driver.quit()