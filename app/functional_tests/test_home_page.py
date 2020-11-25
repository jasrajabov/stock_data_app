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

    def test_fix_genertor_page(self):
        self.browser.get(self.live_server_url)
        expected_url = self.live_server_url + reverse('fixinput')
        self.browser.find_elements_by_xpath('/html/body/div/div/ul/li[2]/a')[0].click()
        assert self.browser.current_url == expected_url

    def test_fix_validator_page(self):
        self.browser.get(self.live_server_url)
        expected_url = self.live_server_url + reverse('fixvalidator')
        self.browser.find_elements_by_xpath('/html/body/div/div/ul/li[3]/a')[0].click()
        assert self.browser.current_url == expected_url

    def test_validate_fix_validator_page_with_data(self):
        self.browser.get(self.live_server_url)
        expected_url = self.live_server_url + reverse('fixvalidator')
        self.browser.find_elements_by_xpath('/html/body/div/div/ul/li[3]/a')[0].click()
        text_box= self.browser.find_element_by_tag_name('textarea')
        text_box.send_keys('8=FIX.4.4|9=121|35=D|34=1|52=20201125-04:32:07.639|60=20201125-04:32:07.639|49=SENDER|56=TARGET|112=TEST|11=FXID1|55=AAPL|54=1|38=1|40=1|10=198')
        self.browser.find_elements_by_xpath('/html/body/div/div/form/button')[0].click()
        result = self.browser.find_elements_by_xpath('/html/body/div/div/div/b')[0].text
        assert result == 'Looks good!'
