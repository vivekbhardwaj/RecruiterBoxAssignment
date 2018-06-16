from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import unittest

class TestBase(unittest.TestCase):
    
    driver = None
    
    def __init__(self,testName,browser):
        
        self.browser = browser
        super(TestBase,self).__init__(testName)
    
    def setUp(self):
        
        if self.browser == "firefox":
            TestBase.driver = webdriver.Firefox()
            
        elif self.browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            TestBase.driver = webdriver.Chrome(chrome_options=options)
        self.url = "https://www.airbnb.co.in/"
        self.driver = TestBase.getdriver()
        TestBase.driver.implicitly_wait(10)
        
    def tearDown(self):
        self.driver.quit()
            
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