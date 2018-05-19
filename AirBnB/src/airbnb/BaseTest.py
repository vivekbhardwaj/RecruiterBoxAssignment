'''
Created on 17-May-2018

@author: Vivek Pathak

This python class deals with the common functionalities needed by each test case
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions

class TestBase():
    
    driver = None
    def __init__(self, browser):
        if browser == "firefox":
            TestBase.driver = webdriver.Firefox()
        elif browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            TestBase.driver = webdriver.Chrome(chrome_options=options)
        TestBase.driver.implicitly_wait(10)
            
    @staticmethod
    def getdriver():
        return TestBase.driver
    
    @staticmethod
    def waitForElementVisibility(locator, expression, message):
        try:
            WebDriverWait(TestBase.driver, 20).\
                until(EC.presence_of_element_located((locator, expression)),
                   message)
            return True
        except:
            return False