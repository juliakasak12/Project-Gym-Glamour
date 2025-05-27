from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPageLocators:
    """
          Search Results Page locators
          """
    PRODUCT = (By.CLASS_NAME, "product-inner-wrap")


class SearchResultsPage(BasePage):
    def click_product(self):
        el = self.driver.find_element(*SearchResultsPageLocators.PRODUCT)
        self.wait_5s.until((EC.element_to_be_clickable(el)))
        el.click()







