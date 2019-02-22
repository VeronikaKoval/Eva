import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Header(BasePage):

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

    feedback_link = (By.CSS_SELECTOR, 'div.block-call-back')
    phone_num_field = (By.CSS_SELECTOR, 'input.call-request-input')
    success_phone_valid = (By.CSS_SELECTOR, 'div.js-submit-result-call-back')
    error_invalid_ph = (By.CSS_SELECTOR, 'span.js-phone-error')

    search_field = (By.CSS_SELECTOR, 'input[id="search"]')
    search_results_block = (By.CSS_SELECTOR, 'div.searchautocomplete__autocomplete')
    empty_search_results_block = (By.CSS_SELECTOR, 'div.empty-result')

    our_projects_block = (By.CSS_SELECTOR, 'span.eva-icon-arr-down')
    drop_down_block_our_projects = (By.CSS_SELECTOR, 'ul.block-mozayka ')
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
    linejka_tovarov = (By.CSS_SELECTOR, 'div.new-banners-wrap')
    naboru_block = (By.CSS_SELECTOR, 'div.collecting-wrap')
    brands_block = (By.CSS_SELECTOR, 'div.brands-wrap')

    subscribe_field = (By.CSS_SELECTOR, 'input#newsletter')
    subscribe_btn = (By.CSS_SELECTOR, 'button[title="Подписаться"]')
    subscription_error = (By.CSS_SELECTOR, 'div#newsletter-error')
    subscription_success = (By.CSS_SELECTOR, 'div.page.messages')

    stores_tab = (By.CSS_SELECTOR, 'a[href$="stockists/"]')
    news_tab = (By.CSS_SELECTOR, 'a[href$="novosti/"]')
    help_tab = (By.CSS_SELECTOR, 'a.js-show-help')
    help_popup = (By.CSS_SELECTOR, 'ul.block-help-links')

    certificate_tab = (By.CSS_SELECTOR, 'a.present-certificate-link')
    certificate_popup = (By.CSS_SELECTOR, 'div.block-card__center')

    wishlist_btn = (By.CSS_SELECTOR, 'span.wishlist')
    cart_btn = (By.CSS_SELECTOR, 'div.minicart-wrapper')
    cart_popup = (By.CSS_SELECTOR, 'div.block.block-minicart.empty')

    uhod_za_soboj_tab = (By.CSS_SELECTOR, 'a[href$="/uhod-soboj/"].top-level-a')
    logo = (By.CSS_SELECTOR, 'a.logo')

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

    def is_search_field_present(self):
        """Checking if the search field is present"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        return self.is_element_present(self.search_field)

    def enter_query_into_seqrch_field(self, query):
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

    def is_our_projects_present(self):
        """ Clicking on the 'Наши проекты' button, Checking the presence of "Our projects" block'"""
        self.wait.until(EC.presence_of_element_located(self.our_projects_block)).click()
        return self.is_element_present(self.drop_down_block_our_projects)

    def is_main_drop_down_menu_present(self):
        """ Clicking on 'Все разделы' menu item, checking the presence of the side drop down menu """
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
        return self.is_element_present(self.left_side_menu)

    # def hover_menu_items(self):
    #     """ Hovering over menu items from left side menu and che checking drop down menu"""
    #     self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
    #     time.sleep(2)
    #     self.wait.until(EC.presence_of_element_located(self.menu_item)).click()
    #     time.sleep(2)
    #     self.hover_element(self.uhod_mi)
    #     self.hover_element(self.parfumeria_mi)
    #     self.hover_element(self.tovary_dlja_doma_mi)
    #     self.hover_element(self.himija_mi)
    #     self.hover_element(self.aksesuaru_mi)
    #     self.hover_element(self.kosmetika_dekorat_mi)
    #     self.hover_element(self.dlja_muzchin_mi)
    #     self.hover_element(self.odezda_mi)
    #     self.hover_element(self.bizhuterija_mi)
    #     self.hover_element(self.dlja_ditej_mi)
    #     try:
    #         self.wait.until(EC.presence_of_element_located(self.drop_down_menu))
    #         return True
    #     except:
    #         return False

    def is_pokupajte_vigodno_present(self):
        """ Checking is product block present"""
        return self.is_element_present(self.product_block)

    def is_linejka_tovarov_present(self):
        """ Checking presence of the block "Linejka tovarov" """
        return self.is_element_present(self.linejka_tovarov)

    def is_nabory_present(self):
        """ Checking presence of the "Nabory" block"""
        return self.is_element_present(self.naboru_block)

    def is_brands_block_present(self):
        """ Checking presence of the "Brands" block """
        return self.is_element_present(self.brands_block)

    def subscribe_for_news(self, email):
        """ Clicking on the subscribe field, entering email"""
        subscribe = self.wait.until(EC.visibility_of_element_located(self.subscribe_field))
        subscribe.click()
        subscribe.send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.subscribe_btn)).click()
        return self

    def get_error_msg_text_newsletters(self):
        """ Getting error message text after subscribing for news with invalid email,
         :return: text of the error message"""
        return self.wait.until(EC.visibility_of_element_located(self.subscription_error)).text

    def get_success_msg_text_newsletters(self):
        """ Getting error message text after subscribing for news with valid email,
                 :return: text of the success message"""
        return self.wait.until(EC.visibility_of_element_located(self.subscription_success)).text

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
        self.wait.until(EC.presence_of_element_located(self.help_tab)).click()
        return self.is_element_present(self.help_popup)

    def click_certificate_tab(self):
        """  Opening the "Certificate" tab and verifying the popup is opened"""
        self.wait.until(EC.presence_of_element_located(self.certificate_tab)).click()
        return self.is_element_present(self.certificate_popup)

    def checking_wishlist(self):
        """ Opening the 'Wishlist' as unregestered user, :return: page current url to verifying that it isn't available for unregistered account"""
        self.wait.until(EC.presence_of_element_located(self.wishlist_btn)).click()
        return self.driver.current_url

    def checking_cart(self):
        """ Opening the 'Cart' and verifying that it is empty for unregistered account"""
        self.wait.until(EC.presence_of_element_located(self.cart_btn)).click()
        return self.wait.until(EC.text_to_be_present_in_element(self.cart_popup, 'ВАША КОРЗИНА ПУСТА!'))

    def checking_logo(self):
        """ Opening the "Uhod" tab, clicking on the logo to verify that it returns to the main page"""
        self.wait.until(EC.presence_of_element_located(self.confirm_location_btn)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.uhod_za_soboj_tab)).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.logo)).click()
        return self.driver.current_url