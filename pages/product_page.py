from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ProductPageLocators:
    GREEN_COLOR = (By.XPATH,'//div[@data-product-id="1121"]')
    XS_SIZE = (By.CLASS_NAME,'radio-wrap')

class ProductPage(BasePage):

    def change_color(self):
        # 1.Znajdź kolor GREEN
        el = self.driver.find_element(*ProductPageLocators.GREEN_COLOR)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2.Kliknij w niego
        el.click()
    def choose_size(self,value):
        el = self.driver.find_element(*ProductPageLocators.XS_SIZE)

        el.send_keys(value)


