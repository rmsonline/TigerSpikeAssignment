'''
Created on Mar. 2018

@author: Ranjith
'''
from TigerSpike.amazon import checkoutPage
import time

class cartPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        
    def get_item_price_in_cart(self):
        self.item_price = self.driver.find_element_by_xpath(
            "//*[contains(text(), 'Subtotal (')]/following-sibling::span[1]").text
        return self.item_price
    
    def get_item_name_in_cart(self):
        self.item_name = self.driver.find_element_by_css_selector("*[class='a-size-medium sc-product-title a-text-bold']").text
        return self.item_name
    
    def validate_item_in_cart(self, item_name, item_price):        
        assert self.item_price == item_price
        assert self.item_name == item_name
        return True
    
    def proceed_to_checkout(self):
        time.sleep(2)
        self.driver.find_element_by_name("proceedToCheckout").click()
        return checkoutPage.checkoutPage(self.driver)
        
        
        
        
    







