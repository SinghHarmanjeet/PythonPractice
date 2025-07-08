from selenium.webdriver.common.by import By
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.TestData import testData
from utils.Locators import locators
from pages.BasePage import BasePage

class login_erp(BasePage):
    def __init__(self):
        super().__init__()
        
    def login(self):
        username = self.driver.find_element(By.ID, locators["username"])
        username.send_keys(testData["username"])
        
        password = self.driver.find_element(By.ID, locators["password"])
        password.send_keys(testData["password"])

        signin_button = self.driver.find_element(By.ID, locators["signinButton"])
        signin_button.click()

        time.sleep(2)

# if __name__ == "__main__":
#     # Create instance and login
#     loginerp = login_erp()
#     loginerp.login()
    





