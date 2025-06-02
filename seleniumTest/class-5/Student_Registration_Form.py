import time
from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

time.sleep(4)
# Maximize the window
driver.maximize_window()

# Wait for the page to load
driver.implicitly_wait(10)

# Fill in the form
driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "email").send_keys("john@gmail.com")  # Intentionally leaving email blank to test validation
time.sleep(2)

driver.find_element(By.XPATH, "//div[3]//div[1]//div[1]//div[3]//input[1]").click()
time.sleep(2)
driver.find_element(By.ID, "mobile").send_keys("98765432102")

driver.find_element(By.ID, "dob").send_keys("01/01/1990")
time.sleep(2)

driver.find_element(By.ID, "subjects").send_keys("subjects: 123 Main St, City, Country")

driver.find_element(By.ID, "hobbies").click()
time.sleep(2)

#driver.find_element(By.ID, "picture").click()
driver.find_element(By.CSS_SELECTOR, "textarea[id='picture']").send_keys("123 Main St, City, Country")

Select(driver.find_element(By.ID, "state")).select_by_index(1)  # Select the first state from the dropdown

time.sleep(2)
Select(driver.find_element(By.ID, "city")).select_by_index(1)  # Select the first city from the dropdown

driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
time.sleep(2)
driver.quit()