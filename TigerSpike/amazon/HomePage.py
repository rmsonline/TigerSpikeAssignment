'''
Created on Mar. 2018

@author: Ranjith
'''
from selenium import webdriver
from TigerSpike.amazon import shopAllPage

class BasePage(object):
    
    def __init__(self,url,browser):
        self.url = url
        self.browser = browser
        if self.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif self.browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif self.browser == 'IE':
            self.driver = webdriver.Ie()
        
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        
    def __del__(self):
        #close the browser
        self.driver.close() 
        
    def login(self, username, password):
        your_account = self.driver.find_element_by_id("nav-link-yourAccount")
        your_account.click() #click on sign in page
        
        email_field = self.driver.find_element_by_id("ap_email")
        continue_btn = self.driver.find_element_by_id("continue")
        email_field.send_keys(username) #enter the email id / username
        continue_btn.click() 
        
        password_btn = self.driver.find_element_by_id("ap_password")
        login_btn = self.driver.find_element_by_id("signInSubmit")
        password_btn.send_keys(password)
        login_btn.click()
            
    def get_page_object_from_home(self, pagename):
        shop_by_dpt = self.driver.find_element_by_id("nav-link-shopall")
        
        if pagename == "shop_all":
            shop_by_dpt.click()
            return shopAllPage.shopAllPage(self.driver) 
        