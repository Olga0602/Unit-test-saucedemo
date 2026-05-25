from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/inputs")
# input_el = driver.find_element(By.TAG_NAME, "input")
# print(input_el.text)
# пример поиска вложенного элемента input по классу и по тегу
input_el = driver.find_element(By.CLASS_NAME, "example").find_element(By.TAG_NAME, "input")
# пример поиска элемента по атрибуту
input_el2 = driver.find_element(By.CSS_SELECTOR,"input[type='number']")

input_el2.send_keys("25")

value_input = input_el.get_attribute("value")
print(value_input)


time.sleep(5)
driver.quit()