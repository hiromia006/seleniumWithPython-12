import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Open the URL
driver.get("https://demowebshop.tricentis.com/")

# sleep(3)
time.sleep(3)

# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, ".ico-register").click()
driver.find_element(By.ID, "gender-male").click()
time.sleep(3)

email = "najua" + str(random.randint(1, 1000)) + "@gmail.com"
print("Generated Email: ", email)

driver.find_element(By.ID, "FirstName").send_keys("John")
driver.find_element(By.ID, "LastName").send_keys("Doe")
driver.find_element(By.ID, "Email").send_keys(email)
time.sleep(3)
driver.find_element(By.ID, "Password").send_keys("password123")
driver.find_element(By.ID, "ConfirmPassword").send_keys("password123")
driver.find_element(By.ID, "register-button").click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, ".ico-logout").click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, ".ico-login").click()
time.sleep(5)
driver.find_element(By.ID, "Email").send_keys(email)
driver.find_element(By.ID, "Password").send_keys("password123")
driver.find_element(By.CSS_SELECTOR, "input[value='Log in']").click()
time.sleep(5)

driver.find_elements(By.CSS_SELECTOR, "input[value='Add to cart']")[0].click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "input[id*='add-to-cart-button-']").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "a[class='ico-cart'] span[class='cart-label']").click()
time.sleep(3)

sel=Select(driver.find_element(By.ID, "CountryId"))
sel.select_by_index(1)
time.sleep(3)
driver.find_element(By.ID, "termsofservice").click()
time.sleep()



driver.quit()
