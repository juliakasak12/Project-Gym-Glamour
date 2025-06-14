from tests.base_test import BaseTest
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from data import test_data_search



class SearchTest (BaseTest):
    def setUp(self):
        super().setUp()
        # Dodatkowy warunek wstępny - wejście na stronę wyszukiwania
        self.search_page = self.home_page.click_search()


    def testEmptySearch(self):
        # (nie wpisujemy nic)
        # 1. Kliknij lupke szukaj
        self.search_page.click_search()


    def testIncorrectSearch(self):
        #(Błędne wyszukiwanie)
        # 1.Wprowadź fraze wyszukiwania
        self.search_page.enter_search(test_data_search.IncorrectSearch.search)
        # 2. Kliknij lupke szukaj
        self.search_page.click_search()


    def testCorrectSearch(self):
        #(Poprawne wyszukiwanie)

        self.product_page = ProductPage(self.driver)
        self.result_page = SearchResultsPage(self.driver)
        # 1.Wprowadź fraze wyszukiwania
        self.search_page.enter_search(test_data_search.CorrectSearch.search)
        # 2. Kliknij lupke szukaj
        self.search_page.click_search()








