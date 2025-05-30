import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Open the URL
driver.get("https://demoqa.com/buttons")

time.sleep(3)
# Maximize the window
driver.maximize_window()
# Wait for the page to load
driver.implicitly_wait(10)

# Actions API allows you to perform complex user interactions like mouse movements, key presses, and drag-and-drop actions.
actions = ActionChains(driver)

# Perform a Double click on the element with ID "doubleClickBtn"
actions.double_click(driver.find_element(By.ID, "doubleClickBtn")).perform()
time.sleep(5)

# Perform a right-click (context click) on the element with ID "rightClickBtn"
actions.context_click(driver.find_element(By.ID, "rightClickBtn")).perform()
time.sleep(5)

driver.get("https://demoqa.com/droppable")
# Perform a drag and drop action from the source element to the target element
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(source, target).perform()
time.sleep(5)

driver.quit()
