from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Scraper:
    def __init__(self, url=""):
        self.pair = ""
        self.currency1_amount = -1

        self.browser = webdriver.Chrome(executable_path="./drivers/chromedriver", chrome_options=webdriver.ChromeOptions())
        self.browser.get(url)
        self.browser.implicitly_wait(10)

        # Buttons
        self.currency_1_btn = self.browser.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div/div[2]/button'
        )
        self.currency_2_btn = self.browser.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div/div[2]/button'
        )
        # Input
        self.currency_1_input = self.browser.find_element_by_xpath(
            '//*[@id="swap-currency-input"]/div/div[2]/input'
        )
        self.currency_2_input = self.browser.find_element_by_xpath(
            '//*[@id="swap-currency-output"]/div/div[2]/input'
        )

    def add_currency(self, contract):
        pass

    def add_currency_and_accept(self, contract):
        pass

    def send_currency_1_amount(self, amount=1):
        self.currency_1_input.click()
        self.currency_1_input.send_keys(str(amount))

    def send_currency_2_amount(self, amount=1):
        self.currency_2_input.click()
        self.currency_2_input.send_keys(str(amount))

    def select_pair(self, currency1, currency2):
        currency1_amount = 1
        # select first currency
        self.currency_1_btn.click()
        token_search = self.browser.find_element_by_id("token-search-input")
        token_search.send_keys(currency1)
        self.browser.implicitly_wait(5)
        token_search.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)

        # select second currency
        self.currency_2_btn.click()
        token_search = self.browser.find_element_by_id("token-search-input")
        token_search.send_keys(currency2)
        self.browser.implicitly_wait(1)
        token_search.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(1)

        if self.pair == "" or currency1_amount != self.currency1_amount:
            self.send_currency_1_amount(amount=currency1_amount)
            self.currency1_amount = currency1_amount

        self.pair = str(currency1) + "/" + str(currency2)

    def get_pair_price(self):
        value = self.currency_2_input.get_attribute("value")
        while value is None or value == "":
            value = self.currency_2_input.get_attribute("value")
        print(value)
        date = datetime.now()
        self.browser.close()
        return str(value)
        """{
            "time": date.strftime("%m/%d/%Y, %H:%M:%S"),
            "value": value,
            "pair": self.pair.replace("/", "_"),
        }
        """