''' Automatyczne wystawianie aukcji Allegro na platformie Baselinker '''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

import time


class Baselinker():

    def __init__(self,e_mail, password, max_count):
        self.e_mail = e_mail
        self.password = password
        self.max_count = max_count
        self.first_time = 0
        self.baselinker_url = "https://login.baselinker.com/"

        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        #Hide Browser
        #self.options.add_argument("--headless")
        self.options.add_argument("--width=1500")
        self.options.add_argument("--height=900")
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        options=self.options,
                                        executable_path=r"C:\\Temp\\geckodriver.exe")

        self.driver.get(self.baselinker_url)
        self.wait = WebDriverWait(self.driver, 100, poll_frequency=1)



    def log_in(self):

        try:
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "loginField")))
            self.driver.find_element_by_id("loginField").send_keys(self.e_mail)
            self.driver.find_element_by_id("passwordField").send_keys(self.password)
            self.driver.find_element_by_id("signinButton").click()
        except Exception as error:  # pylint: disable=broad-except
            print(error)

    def allegro(self):
        try:
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "menu_allegro")))
            self.driver.find_element_by_id("menu_allegro").click()
        except Exception as error:  # pylint: disable=broad-except
            print(error)

    def go_to_allegro(self):
        try:
            time.sleep(5)
            allegro = self.driver.find_elements_by_xpath('//a[@href="/allegro_sell.php"]')[1].click()
        except Exception as error:  # pylint: disable=broad-except
            print(error)

    def filter_amount(self):
        try:
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "category")))

            self.driver.find_element_by_class_name('panel-body').click()
            self.driver.find_element_by_id('products_quantity_from').send_keys('2')
            self.driver.find_element_by_xpath("//input[@value='Ustaw filtr']").click()
            time.sleep(5)
        except Exception as error:  # pylint: disable=broad-except
            print(error)
        try:
            self.wait.until_not(EC.element_to_be_clickable((By.XPATH,'//*[@class="lds-wrapper"]')))
        except Exception as error:  # pylint: disable=broad-except
            print(error)
            time.sleep(40)


    def set_category(self,category):
        self.category = category
        
        try:
            s = Select(self.driver.find_element_by_id("category"))
            s.select_by_visible_text(self.category)

        except Exception as error:  # pylint: disable=broad-except
            print(error)
            return

        try:
            self.wait.until_not(EC.element_to_be_clickable((By.XPATH,'//*[@class="lds-wrapper"]')))
        except Exception as error:  # pylint: disable=broad-except
            print(error)
            self.wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@class="table table-striped table-hover ui-selectable"]')))

        if self.first_time == 0:
            self.filter_amount()
            self.first_time = 1

        try:
            self.driver.find_elements_by_xpath('//*[@class="btn dropdown-toggle tip_trigger"]')[0].click()

            not_auctioned = self.driver.find_element_by_xpath('//*[@onclick="selectNotListed();"]')
            not_auctioned.click()
            self.driver.find_element_by_xpath('//*[@class="bootbox-input bootbox-input-text form-control"]').send_keys(self.max_count)
            time.sleep(3)
        except Exception as error:  # pylint: disable=broad-except
            print(error)
        try:
            sss = self.driver.find_element_by_xpath("//*[text()='Potwierdź']").click()
            time.sleep(3)
            
            self.driver.find_element_by_xpath('//*[@class="btn-label icon fa fa-play"]').click()
            time.sleep(3)
            self.driver.find_elements_by_class_name('lbl')[-1].click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[text()='Przejdź do formularza wystawiania']").click()
            time.sleep(5)
        except Exception as error:  # pylint: disable=broad-except
            print(error)
            return

        try:
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "button_sell_start")))
        except Exception as error:  # pylint: disable=broad-except
            self.driver.find_element_by_xpath('//*[@class="btn btn-default"]').click()
            time.sleep(3)
            return

        try:
            time.sleep(int(self.max_count)*1.5)

            # price = Select(self.driver.find_element_by_id('massive_action'))
            # price.select_by_value('change_price')
            # time.sleep(2)
            # self.driver.find_element_by_xpath('//*[@class="fa fa-chevron-right"]').click()
            # time.sleep(2)
            # self.driver.find_element_by_xpath('//*[@class="bootbox-input bootbox-input-text form-control"]').send_keys('3')
            # time.sleep(2)
            # self.driver.find_element_by_xpath("//*[text()='Potwierdź']").click()
            self.driver.find_element_by_id("button_sell_start").click()
            self.wait.until(EC.text_to_be_present_in_element((By.ID, "progress_bar_percent"), '100%'))

            p = Select(self.driver.find_element_by_xpath
        except Exception as error:  # pylint: disable=broad-except
            print(error)


base = Baselinker(e_mail="",
                password="",
                max_count='20')

list_of_category = ['Accesories', 'Art', 'Audio CD', 'Biography', 'Business', 'Childrens', 'Classics', 'Contemporary', 'Crime', 'Fantasy', 'Fiction', 'Food & Drink', 'Graphic Novel', 'Health & Fitness', 'History', 'Horror', 'Humour & Comedy', 'LGBT', 'Music', 'Mystery', 'Nonfiction', 'Philosophy', 'Poetry', 'Polish Interest', 'Psychology', 'Religion', 'Romance', 'Science', 'Science-Fiction', 'Self Help', 'Sport', 'Thriller', 'Travel', 'Young Adult']

base.log_in()
base.allegro()


for cat in list_of_category:
    base.go_to_allegro()
    base.set_category(cat)

