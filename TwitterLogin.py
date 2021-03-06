import os
import pickle

from selenium import webdriver

class TwitterLogin:
    def __init__(self, username, password, browser_type):
        self.username = username
        self.password = password
        self.browser_type = browser_type
        if "chrome" in browser_type:
            self.browser = webdriver.Chrome("/usr/local/bin/chromedriver")
        else:
            self.browser = webdriver.PhantomJS()

    def LoginWithSelenium(self):
        if os.path.exists("cookies_" + self.browser_type +".pkl"):
            self.browser.get('https://www.twitter.com')
            cookies = pickle.load(open("cookies_" + self.browser_type +".pkl", "rb"))
            for cookie in cookies:
                self.browser.add_cookie(cookie)
            self.browser.refresh()

        else:
            self.browser.get('https://twitter.com/login')
            username_input = self.browser.find_element_by_class_name('js-username-field')
            username_input.send_keys(self.username)

            pass_input = self.browser.find_element_by_class_name('js-password-field')
            pass_input.send_keys(self.password)

            lgbtn = self.browser.find_element_by_xpath("//button[contains(.,'Log in')]")
            lgbtn.click()
            pickle.dump(self.browser.get_cookies(), open("cookies_" + self.browser_type +".pkl", "wb"))

        return self.browser

