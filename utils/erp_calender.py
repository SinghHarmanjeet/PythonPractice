from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
from utils.Locators import locators
import time
import allure
from utils.logger_config import setup_logger

logger = setup_logger('erp_calender')

@allure.step("Select a specific date (today)")
def erpcalender(self):
    selectdate_field = self.driver.find_element(By.XPATH, locators["selectDate"])
    selectdate_field.click()
    time.sleep(2)

    future_date = datetime.now()
    day = future_date.day

    date_element = self.driver.find_element(
        By.XPATH, f"//td[not(contains(@class, 'ng-tns-c3821894747-207 p-datepicker-other-month ng-star-inserted'))]//span[normalize-space()='{day}']"
    )

    if date_element.is_displayed():
        date_element.click()
        time.sleep(2)

@allure.step("Select previous day's date")
def previousday(self):
    logger.info("Selecting previous day's date")
    selectdate_field = self.driver.find_element(By.XPATH, locators["filltimesheet_selectdate"])
    selectdate_field.click()
    time.sleep(2)

    future_date = datetime.now() - timedelta(days=1)
    day = future_date.day
    logger.info(f"Attempting to select date: {day}")

    date_element = self.driver.find_element(By.XPATH,f"//td[not(contains(@class, 'ng-tns-c3821894747-93 p-datepicker-other-month ng-star-inserted'))]//span[normalize-space()='{day}']")

    if date_element.is_displayed():
        date_element.click()
        logger.info(f"Successfully selected date: {day}")
    else:
        logger.warning(f"Date element for {day} is not displayed")
    
@allure.step("Select today's date")
def today(self):
    logger.info("Selecting today's date")
    selectdate_field = self.driver.find_element(By.XPATH, locators["filltimesheet_selectdate"])
    selectdate_field.click()
    time.sleep(2)
    future_date = datetime.now()
    day = future_date.day
    logger.info(f"Attempting to select date: {day}")

    date_element = self.driver.find_element(By.XPATH,f"//td[not(contains(@class, 'ng-tns-c3821894747-93 p-datepicker-other-month ng-star-inserted'))]//span[normalize-space()='{day}']")

    if date_element.is_displayed():
        date_element.click()
        logger.info(f"Successfully selected date: {day}")
    else:
        logger.warning(f"Date element for {day} is not displayed")