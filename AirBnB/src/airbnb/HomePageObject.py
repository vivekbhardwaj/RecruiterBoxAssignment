'''
Created on 17-May-2018

@author: Vivek Pathak

This python class deals with the operations on homepage
'''
from airbnb.BaseTest import TestBase
from selenium.webdriver.common.by import By
from airbnb.FilterPageObject import FilterPage

class HomePage(TestBase):


    def __init__(self):
        self.driver = TestBase.getdriver()
    
    #This method searches for a place i.e, 'Sicily,Italy'
    def seachPlace(self,place):
        if TestBase.waitForElementVisibility(By.ID, "GeocompleteController-via-SearchBarV2-SearchBarV2",
                                                    "Search box is not visible even after witing for 15 seconds.."):
            textBox = self.driver.find_element_by_id("GeocompleteController-via-SearchBarV2-SearchBarV2")
            textBox.send_keys(place)
            
            '''search button is visible only sometimes as website is showing ambigous behaviour,
             so, next time trying to search from ajax drop down'''
            if TestBase.waitForElementVisibility(By.CLASS_NAME, "_f01unc",
                                                         "Search buton not visible.."):
                print "clicking search button"
                searchButton = self.driver.find_element_by_class_name("_f01unc")
                searchButton.click()
            else:
                ajax_dropDown = self.driver.find_element_by_class_name("_1xr62vlo")
                ajax_dropDown.click()            
            return FilterPage()
        else:
            raise Exception("Search box not visible.. Quitting !")
        