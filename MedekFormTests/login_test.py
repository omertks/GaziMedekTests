import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

CHROME_DRIVER_PATH = './drivers/chromedriver'

LOGIN_URL = 'http://localhost:3000/login' 

EMAIL_CSS_SELECTOR = '#root > div > div > div > form > div:nth-child(1) > input'
PASSWORD_CSS_SELECTOR = '#root > div > div > div > form > div:nth-child(2) > input'
LOGIN_BUTTON_CSS_SELECTOR = '#root > div > div > div > form > div.d-grid.mb-3 > button' # Eğer ID yoksa farklı bir seçici kullanmanız gerekebilir

class SimpleLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_simple_login_flow(self):
        self.driver.get(LOGIN_URL)


        email_input = self.driver.find_element(By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)
        email_input.send_keys('admin@admin.admin') # Kendi e-postanızla değiştirin


        password_input = self.driver.find_element(By.CSS_SELECTOR, PASSWORD_CSS_SELECTOR)
        password_input.send_keys('admin1212') # Kendi şifrenizle değiştirin


        login_button = self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)
        login_button.click()


        time.sleep(30)


        print("Kullanıcı Giriş Testi Tamamlandı.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # unittest.TestCase i kalıtmış tüm sınıfları çalıştır demek