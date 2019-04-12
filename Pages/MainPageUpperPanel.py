import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_components.BasePage import BasePage
from Pages.LoginizationPopUp import LoginPopup


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

    login_btn_header = (By.CSS_SELECTOR, 'a.login-popup')
    personal_account_btn = (By.CSS_SELECTOR, 'a.js-authorization-account-popup.show-desktop')
    personal_account_popup = (By.CSS_SELECTOR, 'div.block-authorization-popup.show-desktop.ui-dialog-content.'
        'ui-widget-content[id="ui-id-10"]')

    our_projects_block = (By.CSS_SELECTOR, 'span.eva-icon-arr-down')
    drop_down_block_our_projects = (By.CSS_SELECTOR, 'ul.block-mozayka ')

    stores_tab = (By.CSS_SELECTOR, 'a[href$="stockists/"]')
    news_tab = (By.CSS_SELECTOR, 'a[href$="novosti/"]')
    help_tab = (By.CSS_SELECTOR, 'a.js-show-help')
    help_popup = (By.CSS_SELECTOR, 'ul.block-help-links')

    certificate_tab = (By.CSS_SELECTOR, 'a.present-certificate-link')
    certificate_popup = (By.CSS_SELECTOR, 'div.block-card__center')

    # Actions

    def click_confirm_suggested_location(self):
        """ Clicking 'Yes' button to confirm the suggested city, :return: object of page"""
        return self.click(self.confirm_location_btn, 'Confirm loc btn')

    def is_confirm_loc_btn_visible(self):
        """ Checking if the "Confirm location" btn is visible,
        :return: True, if button is visible"""
        return self.is_element_visible(self.confirm_location_btn)

    def get_loc_text(self):
        """ Getting the location text from the upper panel, :return: text"""
        return self.wait.until(EC.presence_of_element_located(self.location_top)).text

    def click_choose_another_loc_btn(self):
        """ Clicking "Choose another location" btn in the appeared location popup """
        self.wait.until(EC.presence_of_element_located(self.choose_another_location_btn),
                        'There is no "Choose another location" button').click()
        return self

    def choose_location(self):
        """ Clicking 'Choose another location' button, choosing 'Lviv' city as current city
        from the location drop-down list, :return: object of page"""
        self.click_choose_another_loc_btn()
        self.wait.until(EC.presence_of_element_located(self.Lviv), 'There is no such city as Lviv').click()
        return self

    def get_loc_text_from_popup(self):
        """ Getting the location text from the location popup, after changing the location,
        :return: text"""
        return self.wait.until(EC.presence_of_element_located(self.location_text)).text

    def choose_random_loc(self):
        """ Clicking 'Choose another location' button, choosing random location from the list of locations
        :return: object of page"""
        self.click_choose_another_loc_btn()
        all_cities = self.wait.until(EC.presence_of_all_elements_located(self.each_location))
        one_of_the_cities = random.choice(all_cities)
        one_of_the_cities.click()
        return self

    def is_location_changed_popup_visible(self):
        """ Checking if the popup with changed location is visible,
        :return: True if the popup with chosen random location is visible """
        return self.is_element_visible(self.changed_loc_popup)

    def change_language(self):
        """ Changing the language of the site to Ukrainian on the upper panel, :return: object of page"""
        return self.wait.until(EC.presence_of_element_located(self.select_lang)).click()

    def add_lang_cookies(self):
        """ Adding cookies, which are responsible for choosing UKR language as the main language,
        :return: object of page """
        return self.driver.add_cookie({'name': 'store', 'value': 'default_ukr', 'domain': 'eva.ua'})

    def is_login_btn_visible(self):
        """ Checking if the login button is visible,
        :return: True, if login btn is visible"""
        return self.is_element_visible(self.login_btn_header)

    def open_login_popup(self):
        """ Clicking the login button to open the login PopUp,
         :return: object: LoginPopup"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        return LoginPopup()

    def is_our_projects_visible(self):
        """ Clicking on the 'Наши проекты' button, Checking the presence of "Our projects" block,
        :return: True, if "Our projects" block is visible"""
        self.wait.until(EC.presence_of_element_located(self.our_projects_block)).click()
        return self.is_element_visible(self.drop_down_block_our_projects)

    def click_stores_tab(self):
        """ Clicking the "Stores" tab, :return: object of page"""
        return self.wait.until(EC.presence_of_element_located(self.stores_tab)).click()

    def click_news_tab(self):
        """ Opening the "News" tab, :return: object of page"""
        return self.wait.until(EC.presence_of_element_located(self.news_tab)).click()

    def click_help_tab(self):
        """ Opening the "Help" tab on the upper panel and verifying that popup is opened,
        :return True if the popup is visible"""
        self.wait.until(EC.visibility_of_element_located(self.help_tab)).click()
        return self.is_element_visible(self.help_popup)

    def click_certificate_tab(self):
        """  Opening the "Certificate" tab and verifying the popup is opened,
        :return True if the popup is visible"""
        self.wait.until(EC.presence_of_element_located(self.certificate_tab)).click()
        return self.is_element_visible(self.certificate_popup)

    def is_popup_visible_after_authorization(self):
        """ Clicking on the personal account btn after authorization, checking if the popup visible,
        :return: True, if a popup visible after clicking in your account btn"""
        personal_acc_btn = self.wait.until(EC.presence_of_element_located(self.personal_account_btn))
        personal_acc_btn.click()
        time.sleep(1)
        return self.is_element_visible(self.personal_account_popup)
