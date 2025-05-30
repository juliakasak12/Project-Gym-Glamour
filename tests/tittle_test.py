from tests.base_test import BaseTest

class HomeTest(BaseTest):
    def test_tittle(self):
        driver = self.driver
        page_title = driver.title
        #1.Porównaj tytuł strony internetowej
        self.assertIn("Gym Glamour", page_title, "Page tittle does not contain 'GymGlamour'")