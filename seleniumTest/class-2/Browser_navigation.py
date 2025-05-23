import time

from selenium import webdriver

driver = webdriver.Chrome()
# Open the URL
driver.get("https://www.saucedemo.com/")
# Maximize the window
driver.maximize_window()

# Wait for the page to load
driver.implicitly_wait(10)

# Print the title of the page
print("1st Page: ",driver.title)

# Print the current URL
print("1st Page: ",driver.current_url)
time.sleep(4)

# Navigate to another URL
driver.get("https://demowebshop.tricentis.com/")
# Print the title of the new page
print("2nd Page: ", driver.title)
# Print the current URL
print("2nd Page: ",driver.current_url)
time.sleep(4)

# Navigate back to the previous page
driver.back()
time.sleep(4)

driver.forward()
time.sleep(4)
# Refresh the page
driver.refresh()

driver.quit()
