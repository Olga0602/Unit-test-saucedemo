from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
# поиск элемента по тексту внутри кнопки button
add_btn = driver.find_element(By.XPATH, "//button[text()='Add Element']")
# метод click имитирует нажатие на элемент
for _ in range(3): # если i не исп в коде дальше, i заменятется на _
    add_btn.click()
# поиск элементов по классу added-manually
remove_btns = driver.find_elements(By.CLASS_NAME, "added-manually")

for btn in remove_btns:
    btn.click()
    time.sleep(1)

time.sleep(5)
driver.quit()
