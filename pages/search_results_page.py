from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPageLocators:
    """
          Search Results Page locators
          """
    PRODUCT_BUTTON = (By.XPATH,'//div[@data-product-id="982"]')


class SearchResultsPage(BasePage):
    """
                        Waits max 5 seconds for Product button  and clicks it
                        """
    def click_product(self):
        el = self.driver.find_element(*SearchResultsPageLocators.PRODUCT_BUTTON)
        self.wait_5s.until((EC.element_to_be_clickable(el)))
        el.click()

    def _verify_page(self):
        return








