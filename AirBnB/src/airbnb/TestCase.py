'''
Created on 15-May-2018

@author: Vivek Pathak

The actual test case which inherits unittest and TestBase class 
following Page Object Model design pattern
'''
import unittest
from airbnb.HomePageObject import HomePage
from airbnb.BaseTest import TestBase


class Test(unittest.TestCase,TestBase):

    def setUp(self):
        TestBase("firefox")
        self.url = "https://www.airbnb.co.in/"
        self.driver = TestBase.getdriver()
    
    def tearDown(self):
        self.driver.quit()
            
    def testName(self):
        try:
            self.driver.get(self.url)
            
            h_page = HomePage()
            
            f_page = h_page.seachPlace("Sicily,Italy")
            
            f_page.selectExperience()
            
            f_page.selectTodayDate()
                        
            f_page.selectDateAfterThreeMonths()
                        
            f_page.guestAndPriceSelection()
                        
            f_page.movingToFirstAndThirdPost()
            
        finally:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
