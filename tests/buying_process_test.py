from time import sleep
from faker import Faker
from tests.base_test import BaseTest
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.shopping_card_page import ShoppingCardPage


class SearchTest (BaseTest):
    def setUp(self):
        super().setUp()
        # Dodatkowy warunek wstępny - wejście na stronę wyszukiwania
        self.search_page = self.home_page.click_search()

    def testBuyingHat(self):
        # (Zakup czapki)
        search = "czapka zimowa"
        self.product_page = ProductPage(self.driver)
        self.result_page = SearchResultsPage(self.driver)
        self.shopping_page = ShoppingCardPage(self.driver)
        fake = Faker(locale='pl')
        email = fake.email()
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        adres = fake.street_address()
        kodpocztowy = fake.postcode()
        miasto = fake.city()
        # 1.Wprowadź fraze wyszukiwania
        self.search_page.enter_search(search)
        # 2. Kliknij lupke szukaj
        self.search_page.click_search()
        # 3.Kliknij w produkt
        self.result_page.click_product()
        # 4.Zmień kolor
        self.product_page.change_color()
        # 5.Dodaj do koszyka
        self.product_page.add_to_card()
        sleep(3)
        # 6.Przejdź do koszyka
        self.product_page.go_to_basket()
        # 7.Wybierz metodę dostawy
        self.shopping_page.select_delivery_method()
        #8. Kliknij zamawiam
        self.shopping_page.click_order()
        #9. Kliknij zamów bez rejestracji
        self.shopping_page.order_without_registration()
        #10 Wprowadź email
        self.shopping_page.enter_email(email)
        # 11 Wprowadź imie
        self.shopping_page.enter_name(imie)
        # 12 Wprowadź nazwisko
        self.shopping_page.enter_surname(nazwisko)
        # 13 Wprowadź telefon
        self.shopping_page.enter_phone(telefon)
        # 14 Wprowadź adres
        self.shopping_page.enter_address(adres)
        # 15 Wprowadź kod pocztowy
        self.shopping_page.enter_zipcode(kodpocztowy)
        # 16 Wprowadź miasto
        self.shopping_page.enter_city(miasto)
        # 17.Zaakceptuj regulamin
        self.shopping_page.accept_rules()
        # 18.Przejdź do podsumowania
        self.shopping_page.go_to_summary()
        sleep(2)



