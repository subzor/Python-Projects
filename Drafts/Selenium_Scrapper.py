
from threading import Thread
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select

import time

from amazon_co_uk import Amazon_Co_Uk
from amazon_com import Amazon_Com


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return




class Amazon_Scrapper():

    def __init__(self, item):

        self.item = item

        self.url_lists = []
        
        self.title_list = []
        self.authors_list = []
        self.publisher_list = []
        self.category_list = []
        self.pub_data_list = []
        self.bind_list = []
        self.year_list = []
        self.description_list = []
        self.image_list = []
        self.amazon_dict = {}

        self.amazon_co_uk = Amazon_Co_Uk(self.item)
        self.amazon_com = Amazon_Com(self.item)


        # self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        #Hide Browser
        self.options.add_argument("--headless")
        # self.options.add_argument("--width=1500")
        # self.options.add_argument("--height=900")
        # self.options.add_argument('--log-level=1')
        self.driver = webdriver.Chrome(executable_path=r"C:\\chromedriver.exe", 
                                                options=self.options)

        # self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 100, poll_frequency=1)


    def get_urls(self):


        try:
            co_uk_thread = ThreadWithReturnValue(target=self.amazon_co_uk.get_link)
            co_uk_thread.start()

            com_thread = ThreadWithReturnValue(target=self.amazon_com.get_link)
            com_thread.start()

            co = co_uk_thread.join()
            com = com_thread.join()
        except Exception as error:
            print(error)
            pass


        # co_uk_thread = self.amazon_co_uk.get_link()
        print(co, '\n',com)
        # print(com_thread)


    def get_amazon_dict(self):

        # Book details
        try:
            details = self.driver.find_element_by_id('detailBullets_feature_div')
            details = details.find_elements_by_class_name('a-list-item')
            print(details)

        except Exception as error: # pylint: disable=broad-except
            print(error)


        # Unpacking details
        try:
            for detail in details:
                if "Publisher" in detail.text:
                    pub_info = detail.text
                if "Hardcover" in detail.text or "Paperback" in detail.text:
                    bind = detail.text
                if "ISBN-13" in detail.text:
                    isbn = detail.text
        except Exception: # pylint: disable=broad-except
            pass

        # Find isbn
        print(isbn)
        try:
            isbn = isbn.replace('\n','').replace("-",'').replace(' ', '')
            isbn = isbn.split(':')[1]
            isbn = isbn.replace('\u200e','')
            print(isbn)
        except Exception: # pylint: disable=broad-except
            pass

        try:
            if isbn != self.item:
                return self.amazon_dict
        except Exception: # pylint: disable=broad-except
            isbn = None
            return self.amazon_dict



s = Amazon_Scrapper('9780380792429')

s.get_urls()
# s.get_amazon_dict()