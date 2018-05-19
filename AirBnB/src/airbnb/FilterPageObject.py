'''
Created on 17-May-2018

@author: Vivek Pathak

This python class deals with the operations on FilterPage 
'''
from airbnb.BaseTest import TestBase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time

class FilterPage(TestBase):

    def __init__(self):
        self.driver = TestBase.getdriver()
        
    #This method clicks on the 'experiences' button
    def selectExperience(self):
        xpath = "//div[@class='_pex5ot2'][last()]"
        if TestBase.waitForElementVisibility(By.XPATH, xpath,
                                                       "Experience button is not visible.."):
            experiences = self.driver.find_element_by_xpath(xpath)
            experiences.click()
        else:
            raise Exception('Experiences button was not found.. quitting !')
        
    #This method selects the current date from the picker.    
    def selectTodayDate(self):
        if TestBase.waitForElementVisibility(By.CLASS_NAME, "_uutxinj",
                                                             "Date Guest Price buttons are not visible.."):
            date_guest_price = self.driver.find_elements_by_class_name("_uutxinj")
            date_guest_price[0].click() #for clicking on date selector
        else:
            raise Exception('Date/Guests buttons are not visible.. Quitting !')
        dates = self.driver.find_elements_by_xpath("//div[@class='_1lds9wb'][1]//table//td")
        for start_date in dates:
            if start_date.text == str(datetime.now().strftime("%d")):
                start_date.click()
                break
    
    #This method selects the end date i.e, after 3 months.
    def selectDateAfterThreeMonths(self):
        if TestBase.waitForElementVisibility(By.CLASS_NAME,"_121ogl43","Can't move forward in date picker"):
            for i in range(3):
                self.driver.find_element_by_class_name("_121ogl43").click()
                time.sleep(1)
        else:
            raise Exception("Can't move forward in date")
        day = str(datetime.now().strftime("%d"))
        end_date = self.driver.find_element_by_xpath("//div[@class='_1lds9wb'][1]//table//td[text()='"+day+"']")
        end_date.click()
        
    #This method deals with all guest selection(1 adult, 1 child) and price i.e, approximately half
    def guestAndPriceSelection(self):
        element ="//button[@class='_uutxinj']"
        if TestBase.waitForElementVisibility(By.XPATH, element, "guest/price button might not be visible.."):
            guest_price = self.driver.find_elements_by_xpath(element)
            #Weird ! Have to click it two times to get it to open the pop up for guests
            guest_price[0].click()
            guest_price[0].click()
            guest = self.driver.find_elements_by_xpath("//button[@class='_17cu7xl']/span[@class='_1rwjd1n1']")
            time.sleep(1)
            guest[1].click()
            apply = self.driver.find_element_by_class_name('_b82bweu')
            apply.click()
            time.sleep(1)
            guest_price[1].click()
            time.sleep(1)
            slider = self.driver.find_element_by_xpath("//button[@class='_1nx3jn84'][2]")
            ActionChains(self.driver).click_and_hold(slider).move_by_offset(-90.0, 0.0).click().perform()
            # self.driver.execute_script('arguments[0].setAttribute("aria-valuenow","3384")',slider)
            apply = self.driver.find_element_by_class_name("_b82bweu")
            apply.click()
            time.sleep(1)
        else:
            raise Exception("Guest button is not visible.. Quitting !")
        
    #This method clicks on first and third post and returns back to main page.    
    def movingToFirstAndThirdPost(self):
        posts_visible = TestBase.waitForElementVisibility(By.XPATH, "//a[@class='_j1qvyg']/div[@class='_o71trrf']", "Posts not visible..")
        if posts_visible:
            posts = self.driver.find_elements_by_xpath("//a[@class='_j1qvyg']/div[@class='_o71trrf']")
            parent_tab = self.driver.current_window_handle
            #print self.driver.window_handles
            if len(posts)>2:
                posts[0].click()
                TestBase.waitForElementVisibility(By.CLASS_NAME,"_1l18zhtm", "First post didn't load properly..")
                self.driver.switch_to_window(parent_tab)
                #print self.driver.window_handles
                posts[2].click()
                TestBase.waitForElementVisibility(By.CLASS_NAME,"_1l18zhtm", "Second post didn't load properly..")
                #print self.driver.window_handles
                self.driver.switch_to_window(parent_tab)
        else:
            raise Exception("No posts visible.. Quitting !")
