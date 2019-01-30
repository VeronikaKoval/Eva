import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage


class Header(BasePage):

    # Locators

    confirm_location = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')
    location = (By.CSS_SELECTOR, 'span[data-span="top"]')

    select_lang = (By.CSS_SELECTOR, 'a[href="#"]')

    feedback_link = (By.CSS_SELECTOR, 'div.block-call-back')
    phone_num_field = (By.CSS_SELECTOR, 'input[type="tel"]')
    success_phone_valid = (By.CSS_SELECTOR, 'input.phone-valid]')
    error_invalid_ph = (By.CSS_SELECTOR, 'span.js-phone-error')

    search_placeholder = (By.CSS_SELECTOR, 'input[placeholder="Поиск..."]')
    search_field = (By.CSS_SELECTOR, 'input[id="search"]')
    search_results_block = (By.CSS_SELECTOR, 'div[search_autocomplete]')
    empty_search_results_block = (By.CSS_SELECTOR, 'div.empty-result')

    our_products_block = (By.CSS_SELECTOR, 'span.eva-icon-arr-down')
    mozayka = (By.CSS_SELECTOR, 'a[href="https://mozayka.com.ua/"]')

    left_main_menu = (By.CSS_SELECTOR, 'ul.left-menu.js-left-menu')
    menu_item = (By.CSS_SELECTOR, 'span.top-level-a')
    uhod_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/024/uhod-soboj/"]')
    parfumeria_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/217/parfjumerija/"]')

    # Actions

    def choose_location(self):
        """ Choosing current city"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location)).click()

    def get_loc_text(self):
        """Getting location text"""
        return self.wait.until(EC.presence_of_element_located(self.location)).text

    def change_language(self):
        """ Changing the language of the site"""
        self.wait.until(EC.presence_of_element_located(self.select_lang)).click()

    def get_site_url(self):
        """ Getting the site url"""
        return self.driver.current_url

    def feedback(self):
        """ Clicking on feedback link to get feedback pop up"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.feedback_link)).click()
        time.sleep(2)

    def call_back_invalid(self):
        """ Checking calling back with the invalid phone number"""
        phone_field_form = self.wait.until(EC.presence_of_element_located(self.phone_num_field))
        phone_field_form.click()
        phone_field_form.send_keys('00000000')
        phone_field_form.send_keys(Keys.ENTER)

    def get_error_msg_text(self):
        return self.wait.until(EC.presence_of_element_located(self.error_invalid_ph)).text

    def call_back_valid(self):
        """Checking calling back with valid phone number"""
        phone_field_form = self.wait.until(EC.presence_of_element_located(self.phone_num_field))
        phone_field_form.click()
        phone_field_form.send_keys('000000000')
        phone_field_form.send_keys(Keys.ENTER)

    def successfull_call_back(self):
        # success = self.wait.until(EC.presence_of_element_located(self.success_phone_valid))
        return self.wait.until(EC.presence_of_element_located(self.success_phone_valid))

    def is_placeholder_present(self):
        """Checking if the placeholder is present"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location)).click()
        time.sleep(2)
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_placeholder))
            return True
        except:
            return False

    def check_search(self):
        """ Checking the search field"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location))
        time.sleep(2)
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys('духи')
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_results_block))
            return True
        except:
            return False

    def search_with_invalid_query(self):
        """ Checking search results with the invalid query"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location))
        time.sleep(2)
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys('xdcydcyu')

    def get_error_msg_for_query(self):
        return self.wait.until(EC.visibility_of_element_located(self.empty_search_results_block)).text

    def our_products(self):
        self.wait.until(EC.presence_of_element_located(self.our_products_block)).click()
        self.wait.until(EC.presence_of_element_located(self.mozayka)).click()
        time.sleep(3)

    def main_drop_down_menu(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        try:
            self.wait.until(EC.presence_of_element_located(self.left_main_menu))
            return True
        except:
            return False

    def hover_menu_items(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        uhod_mi = self.wait.until(EC.presence_of_element_located(self.uhod_mi))
        uhod_mi.hover()
        time.sleep(2)
        # self.wait.until(EC.presence_of_element_located(self.uhod_mi)).hover()
        # time.sleep(3)
        # self.wait.until(EC.presence_of_element_located(self.parfumeria_mi)).hover(self.parfumeria_mi)

