from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPageLocators:
    """
        Login Page locators
        """
    LOG_IN_BUTTON = (By.XPATH, '//button[@class="btn-3 login"]')
    EMAIL_INPUT = (By.ID, 'mail_input')
    PASSWORD_INPUT = (By.ID, 'pass_input')
    ALERT = (By.XPATH, '//button[@class="close icon-remove"]')


class LoginPage (BasePage):
        """
        Login Page object
        """
        def enter_email(self, email):
            """
            Enters email
            :param email:
            """
            #1.Znajdź pole email
            el = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
            #2.Wypełnij pole
            el.send_keys(email)

        def enter_password(self, password):
            """
            Enters password
            :param password:
            """
            # 1.Znajdź pole password
            el=self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
            # 2.Wypełnij pole
            el.send_keys(password)

        def click_log_in1(self):
            """
            Waits max 5 seconds for Log in button and clicks it
            """
            #1.Znajdź przycisk login
            el = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
            self.wait_5s.until(EC.element_to_be_clickable(el))
            # 2.Kliknij w niego
            el.click()

        def close_alert(self):
                """
                Close alert (Clicks X)
                """
                #1.Znajdź alert
                el = self.driver.find_element(*LoginPageLocators.ALERT)
                self.wait_5s.until(EC.element_to_be_clickable(el))
                #2.Zamknij go
                el.click()
                sleep(2)

        def _verify_page(self):
            print("Weryfikacja strony logowania")
            self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
            self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.PASSWORD_INPUT))
            log_in_button = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
            self.wait_5s.until(EC.element_to_be_clickable(log_in_button))




