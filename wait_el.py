from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
# объект кот создает ожидание 
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

start_btn = driver.find_element(By.TAG_NAME, "button")
start_btn.click()

# ожидание появления элемента с id = finish
text_hidden = wait.until(expected_conditions.visibility_of_element_located((By.ID, "finish")))
print(text_hidden.text)

time.sleep(5)
driver.quit()