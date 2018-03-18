'''
Created on Mar. 2018

@author: Ranjith
'''
import time

class checkoutPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        
    def delete_element(self):
        self.driver.find_element_by_class_name('a-dropdown-label').click()
        self.driver.find_element_by_link_text('Delete').click()
        
    def validate_initial_checkout_page(self):
        pg_src = self.driver.page_source
        try:
            assert ("Checkout" in pg_src ) 
            assert ("1 item" in pg_src )
            assert ("Step 1 of 3" in pg_src ) 
            assert ("Choose a delivery address" in pg_src )
            assert ("Step 2 of 3" in pg_src ) 
            assert ("Payment method" in pg_src )
            assert ("Step 3 of 3" in pg_src ) 
            assert ("Items and delivery" in pg_src)
            return True
        except:
            return False
        
    def validate_step_1(self):
        pg_src = self.driver.page_source
        try:
            assert ("Step 1 of 3" in pg_src ) 
            assert ("Choose a delivery address" in pg_src )
            current_url = self.driver.current_url
            assert ( "addressselect" in current_url )
            self.driver.find_element_by_id("a-autoid-4").click()
            return True
        except:
            return False
            
    def validate_step_2(self):
        pg_src = self.driver.page_source
        time.sleep(2)
        try:
            assert ("Step 2 of 3" in pg_src ) 
            assert ("Payment method" in pg_src )
            assert ("Your credit cards" in pg_src ) 
            current_url = self.driver.current_url
            assert ( "payselect" in current_url )  
            self.driver.find_element_by_id("continue-top").click()
            return True
        except:
            return False
        
    def validate_step_3(self, itemName, itemPrice):
        pg_src = self.driver.page_source
        try:
            assert ("Step 3 of 3" in pg_src ) 
            assert ("Review items and delivery" in pg_src )
            assert ("Estimated Delivery:" in pg_src ) 
            current_url = self.driver.current_url
            assert ( "spc" in current_url )
            itemNameInCheckout = self.driver.find_element_by_xpath(
                '//*[@class="a-fixed-left-grid-col item-details-right-column a-col-right"]/div[1]/span').text
            assert itemNameInCheckout == itemName
            itemPriceInCheckout = self.driver.find_element_by_xpath(
                '//*[@class="a-fixed-left-grid-col item-details-right-column a-col-right"]/div[2]/span/span/span').text
            assert itemPriceInCheckout == itemPrice
            return True
        except:
            return False
           
            

