from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.search_page import SearchPage


class HomePageLocators:
    """
       Home Page locators
       """
    LOG_IN = (By.CLASS_NAME, "account-toggler")
    ACCEPT_COOKIES = (By.XPATH, "//button[@class='btn-3  btn-red js__accept-all-consents']")
    SEARCH = (By.CLASS_NAME,"search-toggler")


class HomePage(BasePage):
    """
       Home Page object
       """
    def accept_cookies(self):
        """
                Accept cookies
                :return: HomePage instance
                """
        #1.Znajdź przycisk accept cookies
        el=self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES)
        #2.Kliknij w niego
        el.click()
        #3.Zwróc strone główną

        return HomePage(self.driver)

    def click_log_in(self):
        """
                Clicks log in link
                :return: LoginPage instance
                """
        # 1. Znajdź przycisk log in

        el =self.driver.find_element(*HomePageLocators.LOG_IN)
        # 2. Kliknij w niego
        el.click()
        # 3.Zwróć stronę logowania
        return LoginPage(self.driver)


    def click_search(self):
        """
                   Clicks search in link
                        """
        # 1. Znajdź przycisk search

        el=self.driver.find_element(*HomePageLocators.SEARCH)
        # 2. Kliknij w niego
        el.click()
        # 3.Zwróć stronę wyszukiwania
        return SearchPage(self.driver)









