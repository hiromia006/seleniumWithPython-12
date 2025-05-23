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

# Select the country from the dropdown
country_dropdown = driver.find_element(By.NAME, "country")
sel=Select(country_dropdown)
sel.select_by_index(6)
time.sleep(5)

sel.select_by_value("AMERICAN SAMOA")
time.sleep(5)

sel.select_by_visible_text("ANTIGUA AND BARBUDA")
time.sleep(5)

# Print all the options in the dropdown
all_options = sel.options
for option in all_options:
    print(option.text)

driver.quit()