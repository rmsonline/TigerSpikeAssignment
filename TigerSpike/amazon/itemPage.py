'''
Created on Mar. 2018

@author: Ranjith
'''

from TigerSpike.amazon import cartPage

class itemPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        
    def get_item_name_on_item_page(self):
        self.name = self.driver.find_element_by_id('productTitle').text
        print("item name is - ", self.name) 
        return self.name       

    def add_to_cart(self):
        add_btn = self.driver.find_element_by_id("add-to-cart-button")
        add_btn.click()
        
    def get_item_price_on_item_page(self):
        self.price = self.driver.find_element_by_id('priceblock_saleprice').text
        print("item price is - ", self.price)
        return self.price
        
    def view_cart(self):
        self.driver.find_element_by_id("hlb-view-cart-announce").click()
        return cartPage.cartPage(self.driver)
    
        
        


