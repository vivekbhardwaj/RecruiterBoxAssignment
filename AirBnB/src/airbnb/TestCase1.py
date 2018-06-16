from airbnb.HomePageObject import HomePage
from airbnb.BaseTest import TestBase


class Test(TestBase):
    
    def __init__(self,testName,browser):
        super(Test,self).__init__(testName,browser)
         
    def testName(self):
        try:
            self.driver.get(self.url)
            
            
            h_page = HomePage()
            
            f_page = h_page.seachPlace("Sicily,Italy")
            
            f_page.selectExperience()
            
            #f_page.selectTodayDate()
                        
            #f_page.selectDateAfterThreeMonths()
                        
            #f_page.guestAndPriceSelection()
                        
            #f_page.movingToFirstAndThirdPost()
            
        finally:
            self.driver.quit()
