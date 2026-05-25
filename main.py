from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/abtest")
# поиск элемента по тегу
title = driver.find_element(By.TAG_NAME, "h3")
print(title.text)
paragraphs = driver.find_elements(By.TAG_NAME, "p")

for paragraph in paragraphs:
    print(paragraph.text)

title_with_class = driver.find_element(By.CLASS_NAME, "example").text
print(title_with_class)

# title_with_class2 = driver.find_element(By.CLASS_NAME, "large-4 large-centered columns").text
# print(title_with_class2)
link_el = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print(link_el.text)


print(paragraphs)



time.sleep(5)

driver.quit()