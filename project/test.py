import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor=f'http://localhost:4444/wd/hub',
            desired_capabilities=caps
        )

    def test_google_search_for_youtube(self):
        browser = self.browser
        browser.get('https://www.google.com')
        search_field = browser.find_element_by_name('q')
        search_field.send_keys('youtube')
        search_field.send_keys(Keys.RETURN)
        self.assertIn('youtube', browser.page_source)


    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')
