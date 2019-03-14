import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains


class List(BasePage):

    # Locators
    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')
    country_france = (By.CSS_SELECTOR, 'li[data-label="Франция"]')
    cancel_filter_france = (By.XPATH, '//*[@id="am_shopby_container"]/ol/li/a')
    scroll_btn = (By.CSS_SELECTOR, 'div.ps__scrollbar-y')
    Nivea = (By.CSS_SELECTOR, 'li[data-label="Nivea"]')

    sorting_block = (By.CSS_SELECTOR, 'div.current-sorting')
    sort_price_desc = (By.CSS_SELECTOR, 'a[data-order="desc"][data-sort="price"]')
    sort_price_asc = (By.CSS_SELECTOR, 'a[data-sort="price"][data-order="asc"]')

    left_scroll_btn = (By.CSS_SELECTOR, 'a.ui-slider-handle[style="left: 0%;"]')
    right_scroll_btn = (By.CSS_SELECTOR, 'a.ui-slider-handle[style="left: 100%;"]')
    input_price_field = (By.CSS_SELECTOR, 'input[id="am_shopby_filter_widget_attr_price_from_5c5aecf72cc56"]')
    price_box = (By.CSS_SELECTOR, 'span.f-left-value')

    # Actions

    def apply_filter_country(self):
        """ Opening "Средства для проблемной кожи" page,
        checking checkbox "Франция" in "Страна производства" filter, :return: object of page """
        self.wait.until(EC.presence_of_element_located(self.country_france)).click()
        return self

    def get_country_filter_attr(self):
        """ Opening "Средства для проблемной кожи" page, getting checkbox "Франция"
        in "Страна производства" filter attribute to verify that checkbox is checked,
        :return: True if the checkbox value is checked"""
        value = self.wait.until(EC.presence_of_element_located(self.country_france)).\
            find_element_by_tag_name('input').get_attribute('checked')
        if value == 'true':
            return True
        else:
            return False

    def apply_filter_name(self):
        """ Opening "Средства для проблемной кожи" page, scrolling down to name filter, clicking on "Nivea" checkbox,
        checking the checkbox status to verify that checkbox is checked """
        scroll_element = self.wait.until(EC.presence_of_element_located(self.scroll_btn))
        scroll = ActionChains(self.driver).drag_and_drop_by_offset(scroll_element, 0, 35).perform()
        time.sleep(3)
        self.wait.until(EC.presence_of_element_located(self.Nivea)).click()
        return self

    def get_name_filter_attr(self):
        """ Opening "Средства для проблемной кожи" page, scrolling down name filter, clicking on "Nivea" checkbox,
        checking the checkbox status to verify that checkbox is checked,
        :return: True if the checkbox value is checked"""
        value = self.wait.until(EC.presence_of_element_located(self.Nivea)).\
            find_element_by_tag_name('input').get_attribute('checked')
        if value == 'true':
            return True
        else:
            return False

    def apply_sort_price_decs(self):
        """ Opening the sorting drop down, clicking sorting from expensive to cheap,
         :return: object of page """
        self.wait.until(EC.presence_of_element_located(self.sorting_block)).click()
        self.wait.until(EC.presence_of_element_located(self.sort_price_desc)).click()
        return self

    def apply_sort_price_asc(self):
        """ Opening the sorting drop down, clicking sorting from cheap to expensive,
        :return: object of page """
        self.wait.until(EC.presence_of_element_located(self.sorting_block)).click()
        self.wait.until(EC.presence_of_element_located(self.sort_price_asc)).click()
        return self

    def apply_manual_price_filter(self):
        """ Scrolling page to manual price filter, applying manual filter for sorting products by price,
        :return: object of page """
        self.driver.execute_script("window.scrollTo(0, 1050)")
        left_scroll = self.wait.until(EC.presence_of_element_located(self.left_scroll_btn))
        ActionChains(self.driver).drag_and_drop_by_offset(left_scroll, 105, 0).perform()
        return self

    def get_text_from_price_box(self):
        """ Getting text from price box on price filter,
        :return: text from the price box """
        return self.wait.until(EC.visibility_of_element_located(self.price_box)).text
