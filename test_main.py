from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

import unittest

class TestHeroku(unittest.TestCase):
    def setUp(self):
        options_browser = Options() # cоздание настроек
        options_browser.add_argument("--headless=new") # настройка, кот не открывает браузер во время тестов
        options_browser.add_argument("--window-size=720,480")

        self.driver = webdriver.Chrome(options=options_browser) # функция, кот вызывается перед каждым тестом,чтобы не писать создание драйвера в каждом тесте
    
    def tearDown(self): # функция кот выз после каждого теста
        self.driver.quit()

    def test_main_page(self):
        # driver = webdriver.Chrome() # эмулятор браузера
        self.driver.get("https://the-internet.herokuapp.com/")
        time.sleep(2)
        title = self.driver.title # получили заголовок страницы
        url_page = self.driver.current_url

        self.assertEqual(title, "The Internet")
        self.assertIn("herokuapp", url_page)
       

    def test_abtest(self):
        # driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/abtest")
        # поиск элемента по тегу
        title_page = self.driver.find_element(By.TAG_NAME, "h3").text

        self.assertIn("A/B Test", title_page)
    
    def test_add_remove(self):
        self.driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
        # поиск элемента по тексту внутри кнопки button
        add_btn = self.driver.find_element(By.XPATH, "//button[text()='Add Element']")
        # метод click имитирует нажатие на элемент
        for _ in range(3): # если i не исп в коде дальше, i заменяется на _
            add_btn.click()
        
        buttons_delete = self.driver.find_element(By.ID, "elements").find_elements(By.TAG_NAME, "button")
        self.assertEqual(len(buttons_delete), 3)
        for button in buttons_delete:
            time.sleep(2)
            button.click()
        buttons_new = self.driver.find_element(By.ID, "elements").find_elements(By.TAG_NAME, "button")
        self.assertEqual(len(buttons_new), 0)

    def test_input_el(self):
        self.driver.get("https://the-internet.herokuapp.com/inputs")
        # пример поиска вложенного элемента input по классу и по тегу
        # input_el = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.TAG_NAME, "input")
        # пример поиска элемента по атрибуту
        input_el2 = self.driver.find_element(By.CSS_SELECTOR,"input[type='number']")

        input_el2.send_keys("25")
        value_input = input_el2.get_attribute("value")
        time.sleep(2)
        self.assertEqual("25",value_input)

        input_el2.send_keys("Hello")
        value_input = input_el2.get_attribute("value")
        print("input_value", value_input)
        self.assertEqual("",value_input)




    
if __name__ == "__main__":
    unittest.main()