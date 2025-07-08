from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.TestData import testData
from utils.Locators import locators
from pages.BasePage import BasePage
import allure
from utils.logger_config import setup_logger
import pytest

logger = setup_logger('erp_login')

class TestERPLogin:
    
    def setup_method(self):
        logger.info("Setting up for ERP login test")
        # Create instance of BasePage instead of inheriting
        self.base_page = BasePage()
        self.driver = self.base_page.driver

    def teardown_method(self):
        logger.info("Tearing down ERP login test")
        if hasattr(self, 'driver'):
            self.driver.quit()

    @pytest.mark.erp_login
    @allure.step("Login to ERP")
    def test_erp_login(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="Before Login", attachment_type=allure.attachment_type.PNG)
        logger.info("Starting ERP login")
        username = self.driver.find_element(By.ID, locators["username"])
        username.send_keys(testData["username"])
        allure.attach(self.driver.get_screenshot_as_png(), name="After Username", attachment_type=allure.attachment_type.PNG)
        logger.info("Username entered")

        password = self.driver.find_element(By.ID, locators["password"])
        password.send_keys(testData["password"])
        allure.attach(self.driver.get_screenshot_as_png(), name="After Password", attachment_type=allure.attachment_type.PNG)
        logger.info("Password entered")

        signin_button = self.driver.find_element(By.ID, locators["signinButton"])
        signin_button.click()
        allure.attach(self.driver.get_screenshot_as_png(), name="After Signin Button", attachment_type=allure.attachment_type.PNG)
        logger.info("Signin button clicked")

# if __name__ == "__main__":

#     # Create instance and login
#     erp = ERP()
#     erp.login()
    
#     # Keep the browser open
#     input("Press Enter to close the browser...")





