import time
from random import randint
from select import select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from BasePage import BasePage


class Header(BasePage):

    # Locators

    confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')
    location_top = (By.CSS_SELECTOR, 'span[data-span="top"]')
    choose_another_location_btn = (By.CSS_SELECTOR, 'a[data-role="select-location"]')
    Lviv = (By.XPATH, '//*[@id="ui-id-2"]/div/div[3]/div/a[8]')
    location_text = (By.CSS_SELECTOR, 'span.call-request-question')

    # location_field = (By.CSS_SELECTOR, 'input[data-input="location-select-search"]')
    # list_of_locations = (By.CSS_SELECTOR, 'a.select-city')

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
    drop_down_block_our_products = (By.CSS_SELECTOR, 'ul.block-mozayka ')
    mozayka = (By.CSS_SELECTOR, 'a[href="https://mozayka.com.ua/"]')

    left_side_menu = (By.CSS_SELECTOR, 'ul.left-menu.js-left-menu')
    menu_item = (By.CSS_SELECTOR, 'span.top-level-a')
    uhod_mi = (By.CSS_SELECTOR, 'a[href$="uhod-soboj/"]')
    parfumeria_mi = (By.CSS_SELECTOR, 'a[href$="parfjumerija/"]')
    tovary_dlja_doma_mi = (By.CSS_SELECTOR, 'a[href$="tovary-dlja-doma/"]')
    himija_mi = (By.CSS_SELECTOR, 'a[href$="bytovaja-himija/"]')
    aksesuaru_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/235/aksessuary/"')
    kosmetika_dekorat_mi = (By.CSS_SELECTOR, 'a[href$="kosmetika-dekorativnaja/"]')
    dlja_muzchin_mi = (By.CSS_SELECTOR, 'a[href$="dlja-muzhchin/"]')
    odezda_mi = (By.CSS_SELECTOR, 'a[href$="odezhda-obuv-aksessuary/"]')
    bizhuterija_mi = (By.CSS_SELECTOR, 'a[href$="bizhuterija/"]')
    dlja_ditej_mi = (By.CSS_SELECTOR, 'a[href="https://eva.ua/12536/dlja-detej/"]')
    drop_down_menu = (By.CSS_SELECTOR, 'ul.level-0.submenu.js-submenu.width-banner.mansorny')

    product_block = (By.CSS_SELECTOR, 'div.block-product-tabs')
    product_item = (By.CSS_SELECTOR, 'div.product-item horizontal')
    product_item_title = (By.CSS_SELECTOR, 'a.title')
    product_item_price = (By.CSS_SELECTOR, 'span.price')
    product_item_buy_btn = (By.CSS_SELECTOR, 'button.action.tocart.primary')

    linejka_tovarov = (By.CSS_SELECTOR, 'div.new-banners-wrap')
    naboru_block = (By.CSS_SELECTOR, 'div.collecting-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-wrap')

    subscribe_field = (By.CSS_SELECTOR, 'input#newsletter')
    subscribe_btn = (By.CSS_SELECTOR, 'button[title="Подписаться"]')
    subscription_error = (By.CSS_SELECTOR, 'div#newsletter-error')
    subscription_success = (By.CSS_SELECTOR, 'div.page.messages')

    # Actions

    def confirm_default_location(self):
        """ Choosing current default city"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()

    def get_loc_text(self):
        """Getting location text"""
        return self.wait.until(EC.presence_of_element_located(self.location_top)).text

    def choose_location(self):
        """Choosing your city"""
        # self.wait.until(EC.presence_of_element_located(self.choose_another_location)).click()
        # # self.wait.until(EC.presence_of_element_located(self.location_field)).click()
        # # self.wait.until(EC.presence_of_all_elements_located(self.list_of_locations))
        # random_location = select(self.driver.find_element(self.list_of_locations))
        # random_location.select_by_index(randint(0, len(random_location.options)))
        self.wait.until(EC.presence_of_element_located(self.choose_another_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.Lviv)).click()
        time.sleep(2)
        return self.wait.until(EC.presence_of_element_located(self.location_text)).text

    def change_language(self):
        """ Changing the language of the site"""
        self.wait.until(EC.presence_of_element_located(self.select_lang)).click()

    def get_site_url(self):
        """ Getting the site url"""
        return self.driver.current_url

    def feedback(self):
        """ Clicking on feedback link to get feedback pop up"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
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
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        try:
            self.wait.until(EC.visibility_of_element_located(self.search_placeholder))
            return True
        except:
            return False

    def check_search(self):
        """ Checking the search field"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn))
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
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn))
        time.sleep(2)
        search = self.wait.until(EC.presence_of_element_located(self.search_field))
        search.click()
        search.send_keys('xdcydcyu')

    def get_error_msg_for_query(self):
        return self.wait.until(EC.visibility_of_element_located(self.empty_search_results_block)).text

    def our_products(self):
        self.wait.until(EC.presence_of_element_located(self.our_products_block)).click()
        try:
            self.wait.until(EC.visibility_of_element_located(self.drop_down_block_our_products))
            return True
        except:
            return False

    def main_drop_down_menu(self):
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        try:
            self.wait.until(EC.presence_of_element_located(self.left_side_menu))
            return True
        except:
            return False

    def hover_menu_items(self):
        """ Hovering over menu items from left side menu and che checking drop down menu"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        time.sleep(2)
        self.hover_element(self.uhod_mi)
        self.hover_element(self.parfumeria_mi)
        self.hover_element(self.tovary_dlja_doma_mi)
        self.hover_element(self.himija_mi)
        self.hover_element(self.aksesuaru_mi)
        self.hover_element(self.kosmetika_dekorat_mi)
        self.hover_element(self.dlja_muzchin_mi)
        self.hover_element(self.odezda_mi)
        self.hover_element(self.bizhuterija_mi)
        self.hover_element(self.dlja_ditej_mi)
        try:
            self.wait.until(EC.presence_of_element_located(self.drop_down_menu))
            return True
        except:
            return False

    def product_block_is_present(self):
        """Checking is product block is present"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.product_block))
            return True
        except:
            return False

    # def check_elements_of_product_item(self):
    #     """Checking the presents of title.price, image on the separate product item """
    #     try:
    #         self.wait.until(EC.presence_of_element_located(self.product_item))
    #         self.wait.until(EC.presence_of_element_located(self.product_item_title))
    #         self.wait.until(EC.presence_of_element_located(self.product_item_price))
    #         self.wait.until(EC.presence_of_element_located(self.product_item_buy_btn))
    #         return True
    #     except:
    #         return
    #     False

    def check_linejka_tovarov(self):
        """Checking presence of the block "Linejka tovarov" """
        try:
            self.wait.until(EC.presence_of_element_located(self.linejka_tovarov))
            return True
        except:
            return False

    def check_sets(self):
        """ Checking presence of the "Naboru" block"""
        try:
            self.wait.until(EC.visibility_of_element_located(self.naboru_block))
            return True
        except:
            return False

    def check_brands_block(self):
        """ Checking presence of the "Brands" block """
        try:
            self.wait.until(EC.presence_of_element_located(self.brands_block))
            return True
        except:
            return False

    def subscribe_for_news_unsuccessful(self):
        """ Checking the ability to subscribe for news with the invalid mail"""
        subscribe = self.wait.until(EC.visibility_of_element_located(self.subscribe_field))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", subscribe)
        # time.sleep(2)
        subscribe.click()
        subscribe.send_keys('ruzifawomaheximail.com')
        self.wait.until(EC.visibility_of_element_located(self.subscribe_btn)).click()
        return self.wait.until(EC.visibility_of_element_located(self.subscription_error)).text

    def subscribe_for_news_successful(self):
        """ Checking the ability to subscribe for news with the invalid mail"""
        subscribe = self.wait.until(EC.visibility_of_element_located(self.subscribe_field))
        subscribe.click()
        subscribe.send_keys('baylan.oluwatimilehin@plutocow.com')
        self.wait.until(EC.visibility_of_element_located(self.subscribe_btn)).click()
        return self.wait.until(EC.visibility_of_element_located(self.subscription_success)).text


