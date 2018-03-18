'''
Created on Mar. 2018

@author: Ranjith

This is a test file
'''
import pytest
import time
from TigerSpike import input_data

class TestPages():
    
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class which contains tests.
        """
        pass
        
    def test_1_add_item(self, amazonTest):
        #goto shop all page
        shop_all_pg = amazonTest.get_page_object_from_home("shop_all")
        lptp_pg = shop_all_pg.get_dept_page_object(input_data.shoppingDeptName)
        
        #select required 5 brands
        brands = input_data.brands
        for brand in brands:
            lptp_pg.select_loptop_brand(brand)
            
        #select other specifications    
        lptp_pg.select_ram_memory(input_data.itemSpec)
        
        #open first item in the search results
        time.sleep(1)
        lptp_pg.open_first_item()
        item_pg = lptp_pg.get_item_page()
        
        #get the name and price displayed on items page
        item_price = item_pg.get_item_price_on_item_page()
        item_name = item_pg.get_item_name_on_item_page()
        
        item_pg.add_to_cart()
        
        cart_pg = item_pg.view_cart()
        
        item_price_in_cart = cart_pg.get_item_price_in_cart()
        item_name_in_cart = cart_pg.get_item_name_in_cart()
        
        print("item_price_in_cart = ", item_price_in_cart)
        print("item_name_in_cart = ", item_name_in_cart)
        
        assert item_price == item_price_in_cart
        assert item_name == item_name_in_cart 
        #assert cart_pg.validate_item_in_cart(item_name, item_price) 
            
        chkout_pg = cart_pg.proceed_to_checkout()
        chkout_pg.validate_initial_checkout_page()
        chkout_pg.validate_step_1()
        print("step 1 validation passed")
        time.sleep(2)
        chkout_pg.validate_step_2()
        print("step 2 validation passed")
        time.sleep(2)
        chkout_pg.validate_step_3(item_name, item_price)
        print("step 3 validation passed")
        
        
    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        pass


if __name__ == '__main__':
    pytest.main(['-s', 'test_pages.py'])


