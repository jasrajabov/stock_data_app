from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_home_page(self):
        self.browser.get(self.live_server_url)

        title = self.browser.find_element_by_class_name('col-8')

        assert title.find_element_by_tag_name('h3').text == 'STOCK DATA'
