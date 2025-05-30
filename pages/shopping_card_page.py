from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ShoppingCardPageLocators:
    DELIVERY_BUTTON = (By.XPATH,'//div[@data-shipping-id="20"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class = "btn-3 important order"]')
    WITHOUT_REGISTRATION_BUTTON = (By.XPATH,'//div[@class= "basket-no-register"]')
    EMAIL_INPUT = (By.ID,'input_mail')
    NAME_INPUT = (By.ID,'input_name')
    SURNAME_INPUT = (By.ID, 'input_surname')
    PHONE_INPUT = (By.ID, 'input_phone')
    ADDRESS_INPUT = (By.ID, 'input_other_address')
    ZIPCODE_INPUT = (By.NAME,'zip')
    CITY_INPUT = (By.ID, 'input_city')
    REGULATION_ACCEPT_BUTTON = (By.XPATH,'//label[@for= "additional_4"]')
    SUMMARY_BUTTON = (By.NAME,'button2')


class ShoppingCardPage(BasePage):
    def select_delivery_method(self):
        """
                                Waits max 5 seconds for Delivery button  and clicks it
                                """
        # 1.Znajdź przycisk dostawy
        el = self.driver.find_element(*ShoppingCardPageLocators.DELIVERY_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()
    def click_order(self):
        """
                                Waits max 5 seconds for Order button  and clicks it
                                """
        # 1.Znajdź przycisk zamów
        el = self.driver.find_element(*ShoppingCardPageLocators.ORDER_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def order_without_registration(self):
        """
                                Waits max 5 seconds for Registration button  and clicks it
                                """
        # 1.Znajdź przycisk zamów bez rejestracji
        el = self.driver.find_element(*ShoppingCardPageLocators.WITHOUT_REGISTRATION_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def enter_email(self, email):
        """
        Enters email
        :param email:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.EMAIL_INPUT)
        # 2.Wypełnij pole
        el.send_keys(email)

    def enter_name(self, name):
        """
        Enters name
        :param name:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.NAME_INPUT)
        # 2.Wypełnij pole
        el.send_keys(name)

    def enter_surname(self, surname):
        """
        Enters surname
        :param surname:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.SURNAME_INPUT)
        # 2.Wypełnij pole
        el.send_keys(surname)

    def enter_phone(self, phone):
        """
        Enters phone
        :param phone:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.PHONE_INPUT)
        # 2.Wypełnij pole
        el.send_keys(phone)

    def enter_address(self, address):
        """
        Enters address
        :param address:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.ADDRESS_INPUT)
        # 2.Wypełnij pole
        el.send_keys(address)

    def enter_zipcode(self,zipcode):
        """
        Enters zipcode
        :param zipcode:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.ZIPCODE_INPUT)
        # 2.Wypełnij pole
        #el.send_keys(zipcode)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            el, zipcode)



    def enter_city(self, city):
        """
        Enters city
        :param city:
        """
        # 1.Znajdź pole username
        el = self.driver.find_element(*ShoppingCardPageLocators.CITY_INPUT)
        # 2.Wypełnij pole
        el.send_keys(city)

    def accept_rules(self):
        """
                                Waits max 5 seconds for Accept regulation button  and clicks it
                                """
        # 1.Znajdź akceptuje regulamin
        el = self.driver.find_element(*ShoppingCardPageLocators.REGULATION_ACCEPT_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def go_to_summary(self):
        """
                                Waits max 5 seconds for Summary button  and clicks it
                                """
        # 1.Znajdź przycisk przejdz do podsumowania
        el = self.driver.find_element(*ShoppingCardPageLocators.SUMMARY_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        # 2. Kliknij w niego
        el.click()

    def _verify_page(self):
        return






