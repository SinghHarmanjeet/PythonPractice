from selenium import webdriver
import time

class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://portal.chicmicstudios.in/dashboard")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("document.body.style.zoom='75%'")

__all__ = ['BasePage']




