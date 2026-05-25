from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

import unittest

class TestAuthorization(unittest.TestCase):
    def setUp(self):
        options_browser = Options()# cоздание настроек
        prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}

        options_browser.add_experimental_option("prefs", prefs)

        options_browser.add_argument("--disable-notifications")
        options_browser.add_argument("--disable-save-password-bubble")
        options_browser.add_argument("--disable-features=PasswordLeakDetection")
        self.driver = webdriver.Chrome(options=options_browser) # функция, кот вызывается перед каждым тестом,чтобы не писать создание драйвера в каждом тесте
    # self.driver.get
    def tearDown(self):# функция кот выз после каждого теста
        self.driver.quit()

    def test_login_success(self):
        self.driver.get("https://www.saucedemo.com/")
        # time.sleep(1)
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys("standard_user")
        # time.sleep(1)
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")
        # time.sleep(1)
        add_btn = self.driver.find_element(By.ID, "login-button")
        add_btn.click()
        # time.sleep(2)
        self.assertEqual("https://www.saucedemo.com/inventory.html",self.driver.current_url)  # driver.current_url получить адрес страницы
        
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name ")
        self.assertTrue(len(items)>0)
    

    def test_login_invalid_password(self):
        self.driver.get("https://www.saucedemo.com/")
        # time.sleep(1)
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys("standard_user")
        # time.sleep(1)

        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret")
        # time.sleep(1)

        add_btn = self.driver.find_element(By.ID, "login-button")
        add_btn.click()
        # time.sleep(2)
        self.assertNotIn("inventory.html",self.driver.current_url) # driver.current_url получить адрес страницы

        error_btn = self.driver.find_element(By.TAG_NAME, "h3").text
        self.assertIn("Username and password do not match", error_btn)



    def test_login_by_enter(self):
        self.driver.get("https://www.saucedemo.com/")
        # time.sleep(1)
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys("standard_user")
        # time.sleep(1)
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")
        # time.sleep(1)
        input_password.send_keys(Keys.ENTER)
        # time.sleep(2)
        self.assertEqual("https://www.saucedemo.com/inventory.html",self.driver.current_url)  # driver.current_url получить адрес страницы
        
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name ")
        self.assertTrue(len(items)>0) # можно исп метод assertGreater()
    
        
class TestProducts(unittest.TestCase):
    def setUp(self):
        options_browser = Options()# cоздание настроек
        prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}

        options_browser.add_experimental_option("prefs", prefs)

        options_browser.add_argument("--disable-notifications")
        options_browser.add_argument("--disable-save-password-bubble")
        options_browser.add_argument("--disable-features=PasswordLeakDetection")
        self.driver = webdriver.Chrome(options=options_browser) # функция, кот вызывается перед каждым тестом,чтобы не писать создание драйвера в каждом тесте

    def tearDown(self):
        self.driver.quit()
    def test_all_products(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys("problem_user")
        time.sleep(1)
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")
        time.sleep(1)
        add_btn = self.driver.find_element(By.ID, "login-button")
        add_btn.click()
        time.sleep(1)
        add_btns_add_to_cart = self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        for btn in add_btns_add_to_cart:
            btn.click()
            time.sleep(1)
        count_shopping = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text # цифра на корзинке
        self.assertEqual(len(add_btns_add_to_cart),int(count_shopping)) # сравниваем количество товаров и цифру на корзинке
        time.sleep(2)


    def test_add_all_products_to_cart(self):
        self.driver.get("https://www.saucedemo.com/")
        input_username = self.driver.find_element(By.ID, "user-name")
        input_username.send_keys("problem_user")
        input_password = self.driver.find_element(By.ID, "password")
        input_password.send_keys("secret_sauce")
        add_btn = self.driver.find_element(By.ID, "login-button")
        add_btn.click()
        time.sleep(2)

        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item") # карточки с товарами
        for i in range(len(items)):
            cards = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
            item_name = cards[i].find_element(By.CLASS_NAME, "inventory_item_name")
            item_name_text = item_name.text
            item_price = cards[i].find_element(By.CLASS_NAME, "inventory_item_price").text
            item_name.click()
            time.sleep(1)
            item_open_name = self.driver.find_element(By.CLASS_NAME, "inventory_details_name").text # название в открытой карточке
            item_open_price = self.driver.find_element(By.CLASS_NAME, "inventory_details_price").text # цена в открытой карточке
            self.assertEqual(item_name_text, item_open_name) # сравниваем название товара в списке и в отктытой карточке
            self.assertEqual(item_price, item_open_price) # сравниваем цену тоывара в писке и в отктытой карточке           
            self.driver.back()
            time.sleep(1)

            