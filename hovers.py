from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/hovers")

show_icons = driver.find_elements(By.CLASS_NAME, "figure")
# print(show_icons)
for icon in show_icons:
    # имитация движения мыши пользователя
    ActionChains(driver).move_to_element(icon).perform()
    time.sleep(1)
    name = icon.find_element(By.TAG_NAME, "h5")
    link_profile = icon.find_element(By.TAG_NAME, "a")

    print(link_profile.get_attribute("href"))



    print(name.text)


time.sleep(5)
driver.quit()