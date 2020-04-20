import time
import unittest
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_google_search_for_youtube(self):
        browser = self.browser
        browser.get('https://www.google.com')
        search_box = browser.find_element_by_name('q')
        search_box.send_keys('youtube')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)  # simulate long running test
        self.assertIn('youtube', browser.page_source)

    def tearDown(self):
        self.browser.quit()  # quit vs close?


if __name__ == '__main__':
    unittest.main()
