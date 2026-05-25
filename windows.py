from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

open_window = driver.find_element(By.XPATH, "//a[text()='Click Here']")
open_window.click()

# получить список открытых вкладок
tabs = driver.window_handles

# переходим на конкретную вкладку
driver.switch_to.window(tabs[1])

title = driver.find_element(By.TAG_NAME, "h3").text

# получить адрес страницы
print(driver.current_url)

# получить заголовок вкладки
print(driver.title)
print(title)

time.sleep(5)
driver.quit()