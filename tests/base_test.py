import unittest
from selenium import webdriver
from pages.home_page import HomePage

class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://gymglamour.com/")
        self.home_page = HomePage(self.driver)
        self.home_page.accept_cookies()




    def tearDown(self):
        self.driver.quit()