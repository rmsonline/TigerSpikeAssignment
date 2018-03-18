'''
Created on Mar. 2018

@author: Ranjith
'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TigerSpike.amazon import itemPage
import time 

class laptopsPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 30)
        

    def select_loptop_brand(self, brandName):
        self.wait.until( EC.visibility_of( 
            self.driver.find_element_by_css_selector("*[href*='lbr_brands_browse']") )).click()
        time.sleep(2)
        self.wait.until( EC.visibility_of( 
            self.driver.find_element_by_css_selector("a[title='%s']" %brandName) )).click()
        
    def select_ram_memory(self, memName):
        self.wait.until( EC.visibility_of( 
            self.driver.find_element_by_xpath("//*[contains(text(), '%s')]" %memName) )).click()

    def open_first_item(self):
        time.sleep(1)
        self.wait.until( EC.visibility_of( 
            self.driver.find_element_by_xpath("//*[@id='result_0']/div[1]/div[3]/div[1]/a") )).click()
    
    def get_item_page(self):
        return itemPage.itemPage(self.driver)


