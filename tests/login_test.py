from tests.base_test import BaseTest
from data import test_data_login


class LoginTest(BaseTest):

    def setUp(self):
        super().setUp()
        # Dodatkowy warunek wstępny - wejście na stronę logowania
        self.login_page = self.home_page.click_log_in()



    def testEmptyLogin(self):
        # (nie wpisujemy nic)
        # 1. Kliknij LogIn
        self.login_page.click_log_in1()
        # 2. Zamknij alert
        self.login_page.close_alert()

    def testInvalidLogin(self):
        #(Niepoprawny login)
        # 1. Wpisz login
        self.login_page.enter_email(test_data_login.InvalidLogin.email)
        # 2. Wpisz haslo
        self.login_page.enter_password(test_data_login.InvalidLogin.password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testInvalidPassword(self):
        #(Niepoprawne hasło)
        # 1. Wpisz login
        self.login_page.enter_email(test_data_login.InvalidPassword.email)
        # 2. Wpisz haslo
        self.login_page.enter_password(test_data_login.InvalidPassword.password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testRandomData(self):
        #(Dane z biblioteki Faker)

        # 1. Wpisz login
        self.login_page.enter_email(test_data_login.RandomData.email)
        # 2. Wpisz haslo
        self.login_page.enter_password(test_data_login.RandomData.password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testValidData(self):
        #(Poprawne dane logowania)
        # 1. Wpisz login
        self.login_page.enter_email(test_data_login.ValidData.email)
        # 2. Wpisz haslo
        self.login_page.enter_password(test_data_login.ValidData.password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
