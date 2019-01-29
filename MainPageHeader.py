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



    # Actions

    def choose_location(self):
        """ Choosing current city"""
        choose_city = self.wait.until(EC.presence_of_element_located(self.confirm_location))
        choose_city.click()

    def get_loc_text(self):
        """Getting location text"""
        location = self.wait.until(EC.presence_of_element_located(self.location))
        return location.text

    def change_language(self):
        """ Changing the language of the site"""
        change_lang_btn = self.wait.until(EC.presence_of_element_located(self.select_lang))
        change_lang_btn.click()
        return self

    def get_site_url(self):
        """ Getting the site url"""
        site_url = self.driver.current_url
        return site_url

    def feedback(self):
        """ Clicking on feedback link to get feedback pop up"""
        feedback_btn = self.wait.until(EC.presence_of_element_located(self.feedback_link))
        feedback_btn.click()
        return self

    def call_back_invalid(self):
        """ Checking calling back with the invalid phone number"""
        phone_field_form = self.wait.until(EC.presence_of_element_located(self.phone_num_field))
        phone_field_form.click()
        phone_field_form.send_keys('00000000')
        phone_field_form.send_keys(Keys.ENTER)
        return self

    def get_error_msg_text(self):
        #error = self.wait.until(EC.presence_of_element_located(self.error_invalid_ph))
        #return error.text
        return self.wait.until(EC.presence_of_element_located(self.error_invalid_ph)).text

    def call_back_valid(self):
        """Checking calling back with valid phone number"""
        phone_field_form = self.wait.until(EC.presence_of_element_located(self.phone_num_field))
        phone_field_form.click()
        phone_field_form.send_keys('000000000')
        phone_field_form.send_keys(Keys.ENTER)
        return self

    def successfull_call_back(self):
        # success = self.wait.until(EC.presence_of_element_located(self.success_phone_valid))
        return self.wait.until(EC.presence_of_element_located(self.success_phone_valid))

    def is_placeholder_present(self):
        """Checking if the placeholder is present"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_placeholder))
            return True
        except:
            return False

    def check_search(self):
        """ Checking the search field"""
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys('духи')
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_results_block))
            return True
        except:
            return False

    def search_with_invalid_query(self):
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys('xdcydcyu')
        return self.wait.until(EC.visibility_of_element_located(self.)).text #found and fill in locator

