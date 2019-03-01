import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Panel(BasePage):

    # Locators
    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')
    location_top = (By.CSS_SELECTOR, 'span[data-span="top"]')
    choose_another_location_btn = (By.CSS_SELECTOR, 'a[data-role="select-location"]')
    Lviv = (By.XPATH, '//*[@id="ui-id-2"]/div/div[3]/div/a[8]')
    location_text = (By.CSS_SELECTOR, 'span.call-request-question')
    each_location = (By.CSS_SELECTOR, 'a.select-city')
    changed_loc_popup = (By.CSS_SELECTOR, 'div.block-location-select')
    loc_text_popup = (By.CSS_SELECTOR, 'span.call-request-massage')

    select_lang = (By.CSS_SELECTOR, 'a[href="#"]')

    our_projects_block = (By.CSS_SELECTOR, 'span.eva-icon-arr-down')
    drop_down_block_our_projects = (By.CSS_SELECTOR, 'ul.block-mozayka ')
    # mozayka = (By.CSS_SELECTOR, 'a[href="https://mozayka.com.ua/"]')

    stores_tab = (By.CSS_SELECTOR, 'a[href$="stockists/"]')
    news_tab = (By.CSS_SELECTOR, 'a[href$="novosti/"]')
    help_tab = (By.CSS_SELECTOR, 'a.js-show-help')
    help_popup = (By.CSS_SELECTOR, 'ul.block-help-links')

    certificate_tab = (By.CSS_SELECTOR, 'a.present-certificate-link')
    certificate_popup = (By.CSS_SELECTOR, 'div.block-card__center')

    # Actions
    def confirm_default_location(self):
        """ Clicking 'Ok' button to confirm the suggested city"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn),
            'There is no "Confirm location" button').click()
        return self

    def get_loc_text(self):
        """ Getting the location text from the upper panel, :return: text"""
        return self.wait.until(EC.presence_of_element_located(self.location_top)).text

    def click_choose_another_loc_btn(self):
        self.wait.until(EC.presence_of_element_located(self.choose_another_location_btn),
            'There is no "Choose another location" button').click()
        return self

    def choose_location(self):
        """ Clicking 'Choose another location' button,
        choosing 'Lviv' city as current city from the location drop-down list, :return: main Page"""
        self.click_choose_another_loc_btn()
        self.wait.until(EC.presence_of_element_located(self.Lviv), 'There is no such city as Lviv').click()
        return self

    def get_loc_text_from_popup(self):
        """ Getting the location text from the location popup, after changing the location, :return: text"""
        return self.wait.until(EC.presence_of_element_located(self.location_text)).text

    def choose_random_loc(self):
        """ Clicking 'Choose another location' button, choosing random location from the list of locations """
        self.click_choose_another_loc_btn()

        all_cities = self.wait.until(EC.presence_of_all_elements_located(self.each_location))
        one_of_the_cities = random.choice(all_cities)
        one_of_the_cities.click()
        try:
            self.wait.until(EC.visibility_of_element_located(self.changed_loc_popup))
            return True
        except:
            return False

    def change_language(self):
        """ Changing the language of the site to UKR on the upper panel"""
        self.wait.until(EC.presence_of_element_located(self.select_lang)).click()
        return self

    def get_page_url(self):
        """ Getting the page url, :return: page current URL"""
        return self.driver.current_url

    def is_our_projects_visible(self):
        """ Clicking on the 'Наши проекты' button, Checking the presence of "Our projects" block'"""
        self.wait.until(EC.presence_of_element_located(self.our_projects_block)).click()
        return self.is_element_visible(self.drop_down_block_our_projects)

    def click_stores_tab(self):
        """ Clicking the "Stores" tab, :return: page current URL"""
        self.wait.until(EC.presence_of_element_located(self.stores_tab)).click()
        return self.driver.current_url

    def click_news_tab(self):
        """ Opening the "News" tab and returning page current URL"""
        self.wait.until(EC.presence_of_element_located(self.news_tab)).click()
        return self.driver.current_url

    def click_help_tab(self):
        """ Opening the "Help" tab on the upper panel and verifying that popup is opened """
        self.wait.until(EC.visibility_of_element_located(self.help_tab)).click()
        return self.is_element_visible(self.help_popup)

    def click_certificate_tab(self):
        """  Opening the "Certificate" tab and verifying the popup is opened"""
        self.wait.until(EC.presence_of_element_located(self.certificate_tab)).click()
        return self.is_element_visible(self.certificate_popup)