import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import os

CHROME_DRIVER_PATH = './drivers/chromedriver'

LOGIN_URL = 'http://localhost:3000/login' 

EMAIL_CSS_SELECTOR = '#root > div > div > div > form > div:nth-child(1) > input'
PASSWORD_CSS_SELECTOR = '#root > div > div > div > form > div:nth-child(2) > input'
LOGIN_BUTTON_CSS_SELECTOR = '#root > div > div > div > form > div.d-grid.mb-3 > button' # Eğer ID yoksa farklı bir seçici kullanmanız gerekebilir

CREATE_MEDEK_FORM_BUTTON_CSS_SELECTOR = '#navbarNav > ul > li:nth-child(2) > a'

class SimpleLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_simple_login_flow(self):
        self.driver.get(LOGIN_URL)


        email_input = self.driver.find_element(By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)
        email_input.send_keys('ogretmen@ogretmen.ogretmen') # Kendi e-postanızla değiştirin


        password_input = self.driver.find_element(By.CSS_SELECTOR, PASSWORD_CSS_SELECTOR)
        password_input.send_keys('ogretmen1212') # Kendi şifrenizle değiştirin


        login_button = self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_CSS_SELECTOR)
        login_button.click()


        time.sleep(5)

        create_medek_form_button = self.driver.find_element(By.CSS_SELECTOR, CREATE_MEDEK_FORM_BUTTON_CSS_SELECTOR)
        create_medek_form_button.click()

        time.sleep(2)   
        
        
        kayit_adi = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(1) > input')
        kayit_adi.send_keys('bu form test ile oluşturuldu')
        
        departman_adi = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(2) > input')
        departman_adi.send_keys('test Okul Adı')
        
        yil_donem_adi = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(3) > input')
        yil_donem_adi.send_keys('2024 - 2025 Bahar')
        
        ogretmen_adi = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(4) > input:nth-child(2)')
        ogretmen_adi.send_keys('test Ogretmen Adı')
        
        ogretmen_soyadi = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(4) > input:nth-child(4)')
        ogretmen_soyadi.send_keys('test Ogretmen Soyadı')
        
        ders_selector = self.driver.find_element(By.CSS_SELECTOR, '#root > div > select')
        select = Select(ders_selector)
        select.select_by_value('order')
        
        time.sleep(1)
        
        ders_ad = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(5) > input:nth-child(4)')
        ders_ad.send_keys('test Ders Adı')
        
        
        ders_kod = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(5) > input:nth-child(2)')
        ders_kod.send_keys('test Ders Kodu')
        
        icindekiler = self.driver.find_element(By.CSS_SELECTOR, '#icindekiler')
        icindekiler.send_keys(os.path.abspath('./pdfs/Icindekiler.pdf'))
        
        akts = self.driver.find_element(By.CSS_SELECTOR, '#aktsFormlari')
        akts.send_keys(os.path.abspath('./pdfs/Akts.pdf'))
        
        sinav_imza_cizerge = self.driver.find_element(By.CSS_SELECTOR, '#sinavImzaCizelgeleri')
        sinav_imza_cizerge.send_keys(os.path.abspath('./pdfs/SinavImzaCizelgeleri.pdf'))
        
        sinav_istatistik = self.driver.find_element(By.CSS_SELECTOR, '#sinavIstatistikleri')
        sinav_istatistik.send_keys(os.path.abspath('./pdfs/SinavIstatistik.pdf'))
        
        vize_ss = self.driver.find_element(By.CSS_SELECTOR, '#vizeSorulari')
        vize_ss.send_keys(os.path.abspath('./pdfs/VizeSS.pdf'))
        
        vize_ed = self.driver.find_element(By.CSS_SELECTOR, '#vizeSinavNotlari')
        vize_ed.send_keys(os.path.abspath('./pdfs/VizeED.pdf'))
       
        final_ss = self.driver.find_element(By.CSS_SELECTOR, '#finalSorulari')
        final_ss.send_keys(os.path.abspath('./pdfs/FinalSS.pdf'))
        
        final_ed = self.driver.find_element(By.CSS_SELECTOR, '#finalSinavNotlari')
        final_ed.send_keys(os.path.abspath('./pdfs/FinalED.pdf'))
        
        but = self.driver.find_element(By.CSS_SELECTOR, '#butSorulari')
        but.send_keys(os.path.abspath('./pdfs/BütSS.pdf'))
        
        resmi_not_cizergesi = self.driver.find_element(By.CSS_SELECTOR, '#resmiNotCizelgesi')
        resmi_not_cizergesi.send_keys(os.path.abspath('./pdfs/ResmiNotCizergesi.pdf'))
        
        ders_devam_cizergesi = self.driver.find_element(By.CSS_SELECTOR, '#devamCizelgesi')
        ders_devam_cizergesi.send_keys(os.path.abspath('./pdfs/DersDevmCizergesi.pdf'))
        
        degerlendirme_anketleri = self.driver.find_element(By.CSS_SELECTOR, '#degerlendirmeAnketleri')
        degerlendirme_anketleri.send_keys(os.path.abspath('./pdfs/DersDegerlendirmeAnketleri.pdf'))
        
        time.sleep(1)
        
        submit_btn = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div:nth-child(18) > button.btn.btn-success')
        submit_btn.click()
        
        time.sleep(1)
        
        panel_btn = self.driver.find_element(By.CSS_SELECTOR, '#navbarNav > ul > li:nth-child(1) > a')
        panel_btn.click()

        
        
        time.sleep(30)
        
        print("Kullanıcı Medek Formu Oluşturma Testi Tamamlandı.")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) # unittest.TestCase i kalıtmış tüm sınıfları çalıştır demek