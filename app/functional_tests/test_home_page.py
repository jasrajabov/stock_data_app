from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from .config import chrome_options, WebBrowserCommands, retry_for_webdriver_exception


time.sleep(20)

class TestHomePage(StaticLiveServerTestCase, WebBrowserCommands):

    def setUp(self):
        
        # self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        #self.browser = webdriver.Chrome(r'/usr/local/bin/chromedriver')
        self.browser = webdriver.Remote(command_executor='http://selenium-remote:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.url = 'http://localhost:8000/'
        time.sleep(5)

    def tearDown(self):
        self.browser.close()

    @retry_for_webdriver_exception
    def test_connection(self):
        self.browser.get("http://www.google.com")


    def test_home_page(self):
        #self.browser.get(self.live_server_url)
        c= 0
        while c <= 5:
            try:
                self.go_to_main_page(self.url)
                title = self.browser.find_element_by_class_name('col-8')
                assert title.find_element_by_tag_name('h3').text == 'STOCK DATA'
            except:
                time.sleep(2)
                c += 1

    @retry_for_webdriver_exception
    def test_fix_genertor_page(self):
        self.browser.get(self.url)
        expected_url = self.url + reverse('fixinput')
        self.browser.find_elements_by_xpath('/html/body/div/div/ul/li[2]/a')[0].click()
        assert self.browser.current_url == expected_url

    @retry_for_webdriver_exception
    def test_fix_validator_page(self):
        self.browser.get(self.url)
        expected_url = self.url + reverse('fixvalidator')
        self.browser.find_elements_by_xpath('/html/body/div/div/ul/li[3]/a')[0].click()
        assert self.browser.current_url == expected_url

    @retry_for_webdriver_exception
    def test_validate_fix_validator_page_with_data(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('/html/body/div/div/ul/li[3]/a').click()
        self.browser.implicitly_wait(3)
        text_box= self.browser.find_element_by_tag_name('textarea')
        text_box.send_keys('8=FIX.4.4|9=117|35=D|34=1|52=20201118-05:27:11.398|60=20201118-05:27:11.398|49=SENDER|56=TARGET|112=TEST|11=1|55=AAPL|54=1|38=1|40=1|10=168')
        time.sleep(3)
        self.browser.find_element_by_xpath('/html/body/div/div/form/button').click()
        self.browser.implicitly_wait(3)

        result = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/b'))
        )

        fix_message = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div'))
        )

        assert '8=FIX.4.4|9=117|35=D|34=1|52=20201118-05:27:11.398|60=20201118-05:27:11.398|49=SENDER|56=TARGET|112=TEST|11=1|55=AAPL|54=1|38=1|40=1|10=168' in fix_message.text
        assert result.text == 'Looks good!'

    @retry_for_webdriver_exception
    def test_validate_fix_generator_page(self):
        self.browser.get(self.url)
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/ul/li[2]/a'))
        ).click()
        stock_symbol = self.browser.find_element_by_id('stock_symbol')
        quantity = self.browser.find_element_by_id('quantity')
        side = Select(self.browser.find_element_by_id('side'))
        order_type = Select(self.browser.find_element_by_id('order_type'))

        stock_symbol.send_keys('AAPL')
        quantity.send_keys('1')
        side.select_by_value('Buy')
        order_type.select_by_value('Market')

        self.browser.find_element_by_xpath('/html/body/div/div/form/button').click()
        self.browser.implicitly_wait(3)
        result = self.browser.find_element_by_xpath('/html/body/div/div/div/b').text
        assert 'Success' in result
