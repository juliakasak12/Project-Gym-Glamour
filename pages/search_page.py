from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPageLocators:
    """
        Search Page locators
        """
    SEARCH_INPUT = (By.CLASS_NAME, "search__input")
    SEARCH_BUTTON = (By.XPATH, '//button[@class="js__search-submit-btn search-btn search__input-area-item btn btn-red search__btn-search r--l-flex r--l-flex-vcenter r--l-flex-hcenter"]')


class SearchPage(BasePage):
    """
    Search Page Object
    """

    def enter_search (self,search):
        """
        Enters search
        :param search:
        """
        #1.Znajdź pole wyszukiwania
        el = self.driver.find_element(*SearchPageLocators.SEARCH_INPUT)
        #2.Wypełnij je
        el.send_keys(search)

    def click_search (self):
        """
                    Waits max 5 seconds for Search button and clicks it
                    """
        #1.Znajdź przycisk wyszukiwania
        el = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        #2.Kliknij w niego
        el.click()

    def _verify_page(self):
        print("Weryfikacja strony wyszukiwania")
        self.wait_5s.until(EC.visibility_of_element_located(SearchPageLocators.SEARCH_INPUT))
        search_button = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(search_button))







