from airbnb.BaseTest import TestBase

class Test(TestBase):
    
    def __init__(self,testName,browser):
        super(Test,self).__init__(testName,browser)
         
    def testName(self):
        try:
            self.driver.get(self.url)
            
        finally:
            self.driver.quit()
