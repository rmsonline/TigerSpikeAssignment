'''
Created on Mar. 2018

@author: Ranjith
'''

from TigerSpike.amazon import laptopsPage
from TigerSpike import input_data

class shopAllPage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)        

    def get_dept_page_object(self, pagename):
        laptops_link = self.driver.find_element_by_link_text(input_data.shoppingDeptName)
        
        dict_of_pages = {"Laptops" : [laptops_link, laptopsPage.laptopsPage(self.driver)] }
                
        dict_of_pages[pagename][0].click()
        return dict_of_pages[pagename][1]

