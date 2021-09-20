from selenium import webdriver
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.headless = False

def retry_for_webdriver_exception(func):
    def wrapper():
        count = 0
        while count <=5:
            try:
                func()
            except WebDriverException:
                time.sleep(2)
                count += 1
        return wrapper



class WebBrowserCommands:

    def __init__(self, browser):
        self.browser = browser

    def go_to_main_page(self, url):
        return self.browser.get(url)