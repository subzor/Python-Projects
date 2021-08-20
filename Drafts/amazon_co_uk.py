from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

import time


class Amazon_Co_Uk():

    def __init__(self,isbn):
        self.isbn = isbn
        self.url_lists = []
        self.amazon_url = f"https://www.amazon.co.uk/s?k={self.isbn}&ref=nb_sb_noss"

        # self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        #Hide Browser
        self.options.add_argument("--headless")
        # self.options.binary_location=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # self.options.add_argument("--width=1500")
        # self.options.add_argument("--height=900")

        # self.options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\danci\OneDrive\Dokumenty\GitHub\Python-Projects\Drafts\chromedriver.exe", 
                                                options=self.options)


        # self.driver = webdriver.Firefox(firefox_profile=self.profile,
        #                         firefox_options=self.options,
        #                         executable_path=r"C:\\Temp\\geckodriver.exe")

        self.driver.get(self.amazon_url)
        self.wait = WebDriverWait(self.driver, 100, poll_frequency=1)

    def get_link(self):

        try:
            self.wait.until(EC.presence_of_all_elements_located((By.ID, "rhf-container")))
            div = self.driver.find_elements_by_xpath('//*[@class="s-main-slot s-result-list s-search-results sg-row"]')
            span_list = div[0].find_elements_by_class_name('a-link-normal')

            links = []
            for i in span_list:
                links.append(i.get_attribute("href"))

        except Exception as error:
            print("Get link - find url: ",error)

        try:
            links = list(set(links))
        except Exception as error:
            print("Get link - set to list: ",error)

        try:
            for link in links:
                if f'keywords={self.isbn}' in link:
                    self.url_lists.append(link)
        except Exception as error:
            print("Get link - loop on links: ",error)

        return self.url_lists

# s = Amazon_Co_Uk('9780380792429')
# lol = s.get_link()

# print(lol)