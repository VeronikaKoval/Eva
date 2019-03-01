
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Header(BasePage):

    # Locators
    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')

    feedback_link = (By.CSS_SELECTOR, 'div.block-call-back')
    phone_num_field = (By.CSS_SELECTOR, 'input.call-request-input')
    success_phone_valid = (By.CSS_SELECTOR, 'div.js-submit-result-call-back')
    error_invalid_ph = (By.CSS_SELECTOR, 'span.js-phone-error')

    search_field = (By.CSS_SELECTOR, 'input[id="search"]')
    search_results_block = (By.CSS_SELECTOR, 'div.searchautocomplete__autocomplete')
    empty_search_results_block = (By.CSS_SELECTOR, 'div.empty-result')

    wishlist_btn = (By.CSS_SELECTOR, 'span.wishlist')
    cart_btn = (By.CSS_SELECTOR, 'div.minicart-wrapper')
    cart_popup = (By.CSS_SELECTOR, 'div.block.block-minicart.empty')
    cart_popup_msg = (By.CSS_SELECTOR, 'strong.subtitle.empty')

    uhod_za_soboj_tab = (By.CSS_SELECTOR, 'a[href$="/uhod-soboj/"].top-level-a')
    logo = (By.CSS_SELECTOR, 'a.logo')

    # Actions

    def call_back(self, phone_number):
        """ Clicking on feedback link to get feedback pop up, clicking on the phone field """
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.feedback_link)).click()
        phone_field_form = self.wait.until(EC.presence_of_element_located(self.phone_num_field))
        phone_field_form.click()
        phone_field_form.send_keys(phone_number)
        phone_field_form.send_keys(Keys.ENTER)
        return self

    def get_error_text_with_invalid_number(self):
        """ Checking call back functionality with the invalid phone number,
         :return: text of the error after entering the invalid phone number """
        return self.wait.until(EC.presence_of_element_located(self.error_invalid_ph)).text

    def get_successful_msg_text_with_valid_number(self):
        """  Checking call back functionality with the valid phone number,
         :return: text of the success message after entering the valid phone number """
        return self.wait.until(EC.presence_of_element_located(self.success_phone_valid)).text

    def is_search_field_visible(self):
        """Checking if the search field is present"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        return self.is_element_visible(self.search_field)

    def enter_query_into_search_field(self, query):
        """ Clicking on the search field and entering search query """
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys(query)
        return self

    def is_search_result_block_present(self):
        """ Clicking on the search field, entering valid search query
        and checking whether the block with search results is present"""
        return self.is_element_present(self.search_results_block)

    def get_error_msg_for_invalid_query(self):
        """ Clicking on the search field, entering invalid search query,
        :return: text of the error for the invalid query """
        return self.wait.until(EC.visibility_of_element_located(self.empty_search_results_block)).text

    def get_page_url(self):
        """ Getting the page url, :return: page current URL"""
        return self.driver.current_url

    def open_wishlist(self):
        """ Opening the 'Wishlist' as unregestered user,
        :return: page current url to verifying that it isn't available for unregistered account"""
        self.wait.until(EC.presence_of_element_located(self.wishlist_btn)).click()
        return self

    def open_cart(self):
        """ Opening the 'Cart', verifying that cart popup is opened
        and it is empty for unregistered account"""
        self.wait.until(EC.presence_of_element_located(self.cart_btn)).click()
        return self.is_element_visible(self.cart_popup)

    def get_text_from_cart_popup(self):
        """ Opening cart popup as unregestered user, getting text from popup, :return: text"""
        return self.wait.until(EC.visibility_of_element_located(self.cart_popup_msg)).text

    def is_logo_visible(self):
        """ Checking if the logo is visible"""
        return self.is_element_visible(self.logo)

    def click_logo(self):
        """ Opening the "Uhod" tab, clicking on the logo to verify that it returns to the main page"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.uhod_za_soboj_tab)).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.logo)).click()
        return self
