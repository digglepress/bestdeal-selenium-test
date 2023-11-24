import time
import unittest

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from logger import with_logs

page_url = "https://bestdealnaija.com/"


class TestProject(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def get_status_code(self) -> int:
        # Get the current page URL
        current_url = self.driver.current_url

        # Use requests to get the status code of the current page URL
        response = requests.get(current_url)

        # Return the status code
        return response.status_code

    def tearDown(self) -> None:
        self.driver.quit()

    @with_logs
    def test_featured_products_should_redirect_to_product_page(self):
        """featured products should redirect to product page"""

        self.driver.get(page_url)
        featured_products = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'slide')]"))
        )
        for product in featured_products:
            product.click()
            self.assertEqual(self.get_status_code(), 200)
        time.sleep(5)

    @with_logs
    def test_featured_products_should_redirects(self):
        """featured products """

        self.driver.get(page_url)
        featured_products = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'slide')]"))
        )
        for product in featured_products:
            product.click()
            self.assertEqual(self.get_status_code(), 200)
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()
