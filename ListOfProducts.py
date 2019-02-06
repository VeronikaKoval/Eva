import time

from selenium.webdriver.common.by import By

from BasePage import BasePage

from selenium.webdriver.support import expected_conditions as EC


class List(BasePage):

    # Locators
    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')
    uhod_mi = (By.CSS_SELECTOR, 'a[href$="uhod-soboj/"]')
    menu_item = (By.CSS_SELECTOR, 'span.top-level-a')
    sredstva_dlja_kozhi_mi = (By.CSS_SELECTOR, 'a[href$="sredstva-problemnoj-kozhi/"]')
    country_france = (By.CSS_SELECTOR, 'li[data-label="Франция"]')
    cancel_filter_france = (By.XPATH, '//*[@id="am_shopby_container"]/ol/li/a')

    # Actions

    def open_category(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.hover_element(self.menu_item)
        time.sleep(2)
        self.hover_element(self.uhod_mi)
        time.sleep(1)
        self.hover_element(self.sredstva_dlja_kozhi_mi)
        self.wait.until(EC.presence_of_element_located(self.sredstva_dlja_kozhi_mi)).click()
        return self.driver.current_url

    def apply_filter_country(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()

        self.hover_element(self.menu_item)
        time.sleep(2)
        self.hover_element(self.uhod_mi)
        time.sleep(1)
        self.hover_element(self.sredstva_dlja_kozhi_mi)
        self.wait.until(EC.presence_of_element_located(self.sredstva_dlja_kozhi_mi)).click()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located(self.country_france)).click()
        time.sleep(2)

        try:
            self.wait.until(EC.presence_of_element_located(self.country_france)).get_attribute('checked')
            return True
        except:
            return False

    def cancel_filter_country(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()

        self.hover_element(self.menu_item)
        # time.sleep(2)
        self.hover_element(self.uhod_mi)
        # time.sleep(1)
        self.hover_element(self.sredstva_dlja_kozhi_mi)
        self.wait.until(EC.presence_of_element_located(self.sredstva_dlja_kozhi_mi)).click()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located(self.country_france)).click()
        time.sleep(5)

        self.wait.until(EC.presence_of_element_located(self.country_france)).click()
        time.sleep(3)

        try:
            self.wait.until(EC.presence_of_element_located(self.country_france)).get_attribute('nofollow')
            return True
        except:
            return False

    # def apply_filter_purpose(self):
