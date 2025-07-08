from selenium.webdriver.common.by import By
import time
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Locators import locators
from utils.TestData import testData
from pages.login_erp import login_erp
from utils.erp_calender import erpcalender
from utils.logger_config import setup_logger
import allure
import pytest

logger = setup_logger('apply_leave')

class TestApplyLeave:
    
    def setup_method(self):
        logger.info("Setting up for ERP login test")
        # Create instance of BasePage instead of inheriting
        self.login_erp = login_erp()
        self.driver = self.login_erp.driver

    def teardown_method(self):
        logger.info("Tearing down ERP login test")
        if hasattr(self, 'driver'):
            self.driver.quit()

    @pytest.mark.apply_leave
    @allure.step("Apply Leave")   
    def test_apply_leave(self):
        
        allure.attach(self.driver.get_screenshot_as_png(), name="Before Login", attachment_type=allure.attachment_type.PNG)
        logger.info("Starting ERP login")
        
        self.login_erp.login()
        
        allure.attach(self.driver.get_screenshot_as_png(), name="After Login", attachment_type=allure.attachment_type.PNG)
        logger.info("Login successful")
        
        time.sleep(2)  

        approval_dropdown = self.driver.find_element(By.CSS_SELECTOR, locators["approvalDropdown"])
        approval_dropdown.click()
        
        time.sleep(2)

        leave_history = self.driver.find_element(By.XPATH, locators["selectApproval"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", leave_history)
        time.sleep(5)
        leave_history.click()

        time.sleep(2)

        apply_leave = self.driver.find_element(By.XPATH, locators["applyLeave"])
        apply_leave.click()

        time.sleep(2)

        leavetype_dropdown = self.driver.find_element(By.XPATH, locators["leaveTypeDropdown"])
        leavetype_dropdown.click()

        time.sleep(2) 

        if leavetype_dropdown.is_enabled:
            leave_type = self.driver.find_element(By.XPATH, locators["leaveType"])
            leave_type.click()

        time.sleep(2)

        leavecategory_dropdown = self.driver.find_element(By.XPATH, locators["leaveCategoryDropdown"])
        leavecategory_dropdown.click()

        time.sleep(2)

        if leavecategory_dropdown.is_enabled:
            leave_category = self.driver.find_element(By.XPATH, locators["leaveCategory"])
            leave_category.click()

        time.sleep(2)

        # Click to open the date picker
        erpcalender(self)
            
        leavereason_dropdown = self.driver.find_element(By.XPATH, locators["leaveReasonDropdown"])
        leavereason_dropdown.click()

        time.sleep(2)

        if leavereason_dropdown.is_enabled:
            leave_reason = self.driver.find_element(By.XPATH, locators["leaveReason"])
            leave_reason.click()

        time.sleep(2)

        leavecomments_box = self.driver.find_element(By.XPATH, locators["leaveComments_box"])
        leavecomments_box.send_keys(testData["leaveComments"])

        time.sleep(2)

        sendto_dropdown = self.driver.find_element(By.XPATH, locators["sendToDropdown"])
        sendto_dropdown.click()

        time.sleep(2)

        sendto_projectmanager = self.driver.find_element(By.XPATH, locators["sendToProjectManager"])
        sendto_projectmanager.click()

        time.sleep(2)

        close_sendto_dropdown = self.driver.find_element(By.XPATH, locators["closeSendToDropdown"])
        close_sendto_dropdown.click()

        time.sleep(2)

        apply_button = self.driver.find_element(By.XPATH, locators["applyButton"])
        apply_button.click()


# if __name__ == "__main__":
    
#     applyleave_erp = applyleave()
#     applyleave_erp.applyLeave()        
    
#     input("Press Enter to close the browser...")
    