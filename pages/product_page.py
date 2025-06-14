from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPageLocators:
    """
            Product Page locators
            """
    BLACK_COLOR_BUTTON = (By.XPATH,'//div[@data-product-id="981"]')
    ADD_TO_CARD_BUTTON = (By.XPATH,'//div[@class="button_wrap"]')
    GO_TO_BASKET_BUTTON = (By.XPATH, '//div[@class="modal-footer"]')

class ProductPage(BasePage):

    def change_color(self):
        """
                   Waits max 5 seconds for Black color button and clicks it
                   """
        # 1.Znajdź kolor czarny
        el = self.driver.find_element(*ProductPageLocators.BLACK_COLOR_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2.Kliknij w niego
        el.click()

    def add_to_card(self):
        """
                   Waits max 5 seconds for Add to card  button and clicks it
                   """
        # 1.Znajdź przycisk dodaj do koszyka
        el = self.driver.find_element(*ProductPageLocators.ADD_TO_CARD_BUTTON)
        self.wait_10s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def go_to_basket(self):
        """
                   Waits max 5 seconds for Go to basket button and clicks it
                   """
        # 1.Znajdź przycisk przejdz do koszyka
        el = self.driver.find_element(*ProductPageLocators.GO_TO_BASKET_BUTTON)
        self.wait_10s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def _verify_page(self):
        return








