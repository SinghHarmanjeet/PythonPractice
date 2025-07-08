import allure
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.Locators import locators
from utils.TestData import testData
from pages.login_erp import login_erp
from utils.logger_config import setup_logger
import pytest
from utils.erp_calender import today, previousday

# Setup logger
logger = setup_logger('fill_timesheet')

@pytest.mark.fill_timesheet
class TestFillTimesheet:
    def setup_method(self):
        logger.info("Setting up for test")
        # Create instance of login_erp instead of inheriting
        self.login_instance = login_erp()
        self.driver = self.login_instance.driver

    def teardown_method(self):
        logger.info("Tearing down test")
        if hasattr(self, 'driver'):
            self.driver.quit()

    
    
     
    @allure.step("Fill timesheet")
    def test_fill_timesheet(self):
        logger.info("Starting test_fill_timesheet")
        try:
            self.login_instance.login()
            allure.attach(self.driver.get_screenshot_as_png(), name="After Login", attachment_type=allure.attachment_type.PNG)
            logger.info("Successfully logged in")

            time.sleep(2)

            project_timesheet = self.driver.find_element(By.XPATH, locators["projectTimesheet"])
            project_timesheet.click()
            logger.info("Clicked on project timesheet")

            time.sleep(2)

            todays_timesheet = self.driver.find_element(By.XPATH, locators["todaysTimesheet"])
            todays_timesheet.click()
            logger.info("Clicked on today's timesheet")

            time.sleep(2)

            time_spent = self.driver.find_element(By.XPATH, "(//b[@id='totalTimeSpent'])[1]")
            total_time_spent = time_spent.text
            logger.info(f"Total time spent: {total_time_spent}")
            
            
            if total_time_spent >= "08:00":
                logger.info("Time spent is 8 hours or more, selecting today's date")
                today(self)
            elif total_time_spent >= "04:00" and total_time_spent < "08:00":
                logger.info("Time spent is between 4 and 8 hours, selecting today's date")
                today(self)
            else:
                logger.info("Time spent is less than 4 hours, selecting previous day's date")
                previousday(self)

            time.sleep(2)

            select_project_dropdown = self.driver.find_element(By.XPATH, locators["selectProjectDropdown"])
            select_project_dropdown.click()
            logger.info("Clicked on project dropdown")

            time.sleep(2)

            select_project = self.driver.find_element(By.XPATH, locators["selectProject"])
            select_project.click()
            logger.info("Selected project")

            time.sleep(2)

            select_task_dropdown = self.driver.find_element(By.XPATH, locators["selectTaskDropdown"])
            select_task_dropdown.click()
            logger.info("Clicked on task dropdown")

            time.sleep(2)

            select_task_type = self.driver.find_element(By.XPATH, locators["selectTaskType"])
            select_task_type.click()
            logger.info("Selected task type")

            time.sleep(2)
            enter_time = self.driver.find_element(By.XPATH, locators["enterTime"])
            if total_time_spent >= "08:00": 
                enter_time.send_keys(testData["enter_time"])
                logger.info(f"Entered time: {testData['enter_time']}")
            elif total_time_spent >= "04:00" and total_time_spent < "08:00":            
                enter_time.send_keys(testData["enter_time_halfday"])
                logger.info(f"Entered time: {testData['enter_time_halfday']}")
            else:
                logger.warning("Time spent is less than 4 hours")
            time.sleep(2)

            timesheet_notes = self.driver.find_element(By.XPATH, locators["timesheetNotes"])
            timesheet_notes.send_keys(testData["timesheetNotes"])
            logger.info("Added timesheet notes")

            time.sleep(2)

            save_button = self.driver.find_element(By.XPATH, locators["saveButton"])
            save_button.click()
            logger.info("Clicked save button")

            time.sleep(2)
            logger.info("Timesheet filling process completed successfully")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
            logger.error(f"An error occurred while filling timesheet: {str(e)}", exc_info=True)
            raise


# if __name__ == "__main__":
#     try:
#         logger.info("Starting timesheet automation")
#         fillTimesheet = TestFillTimesheet()
#         fillTimesheet.test_fill_timesheet()       
#         logger.info("Timesheet automation completed successfully")
#     except Exception as e:
#         logger.error(f"An error occurred in main execution: {str(e)}", exc_info=True)
    
#     input("Press Enter to close the browser...")  



