import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
# Open the URL
driver.get("https://demo.guru99.com/test/newtours/register.php?authuser=0")
time.sleep(3)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

driver.find_element(By.NAME, "firstName").send_keys("John")
driver.find_element(By.NAME, "lastName").send_keys("Doe")
driver.find_element(By.NAME, "phone").send_keys("1234567890")
time.sleep(5)
driver.find_element(By.NAME, "userName").send_keys("adklsa@gmail.com")
driver.find_element(By.NAME, "address1").send_keys("123 Main St")
driver.find_element(By.NAME, "city").send_keys("New York")
driver.find_element(By.NAME, "state").send_keys("NY")
driver.find_element(By.NAME, "postalCode").send_keys("10001")

# Select the country from the dropdown
country_dropdown = driver.find_element(By.NAME, "country")
sel=Select(country_dropdown)
sel.select_by_index(6)
time.sleep(5)

driver.find_element(By.ID, "email").send_keys("dsdfsdf")
driver.find_element(By.NAME, "password").send_keys("password123")
driver.find_element(By.NAME, "confirmPassword").send_keys("password123")

driver.find_element(By.NAME, "submit").click()

time.sleep(5)
driver.quit()