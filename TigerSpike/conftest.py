'''
Created on Mar. 2018

@author: Ranjith
'''

from TigerSpike.amazon import HomePage
import pytest
from TigerSpike import input_data

@pytest.fixture
def amazonTest():
    '''
        pytest fixture which creates BasePage object
        and logs into the amazon site
        This can be used a parameter in the tests
    '''
    amazonHomeObj = HomePage.BasePage(input_data.web_url, input_data.browser)
    amazonHomeObj.login(input_data.username, input_data.password)
    return amazonHomeObj

