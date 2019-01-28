from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage


class Header(BasePage):

    # Locators
    authorization_btn = (By.CSS_SELECTOR, 'div[data-popup-handler="auth"]')
    search_field = (By.CSS_SELECTOR, 'input#search-input')

    # Actions


    def check_search_field(self):
        """ Checking if the search field is clickable"""
        search = self.wait.until(EC.element_to_be_clickable(self.search_field))
        search.send_keys('сухой шампунь')



