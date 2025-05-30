from tests.base_test import BaseTest
from faker import Faker


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
        email = "tester_alk"
        password = "haslo"
        # 1. Wpisz login
        self.login_page.enter_username(email)
        # 2. Wpisz haslo
        self.login_page.enter_password(password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testInvalidPassword(self):
        #(Niepoprawne hasło)
        email = "testeralk8@gmail.com"
        password = "ala123"
        # 1. Wpisz login
        self.login_page.enter_username(email)
        # 2. Wpisz haslo
        self.login_page.enter_password(password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testRandomData(self):
        #(Dane z biblioteki Faker)
        fake = Faker(locale='pl')
        email = fake.email()
        password = fake.password()
        # 1. Wpisz login
        self.login_page.enter_username(email)
        # 2. Wpisz haslo
        self.login_page.enter_password(password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
        # 4. Zamknij alert
        self.login_page.close_alert()

    def testValidData(self):
        #(Poprawne dane logowania)
        email = "testeralk8@gmail.com"
        password = "Testeralk@88"
        # 1. Wpisz login
        self.login_page.enter_username(email)
        # 2. Wpisz haslo
        self.login_page.enter_password(password)
        # 3. Kliknij Log In
        self.login_page.click_log_in1()
