import time

from selenium.common.exceptions import WebDriverException

from BasePage import BasePage

from BaseTest import BaseTest

from selenium.webdriver.common.by import By

from MainPageHeader import Header

class Test(BaseTest):

    # def test_main_page(self):
    #     slider_locator = (By.CSS_SELECTOR, 'div.header-contact div.button')
    #     base_page = BasePage()
    #     base_page.click(slider_locator)
    #
    # def test_search_field_is_clickable(self):
    #     main_page = Header()
    #     search_locator = main_page.search_field
    #     # try:
    #     #     main_page.click(search_locator)
    #     # except WebDriverException:
    #     #     print ('Element is not clickable')

    def test_choose_location(self):
        main_page = Header()
        main_page.choose_location()
        assert 'Киев' in main_page.get_loc_text()

    def test_changing_lang(self):
        main_page = Header()
        main_page.change_language()
        assert 'ua/' in main_page.get_site_url()

    def test_call_back_unsuccessful(self):
        main_page = Header()
        main_page.feedback()\
            .call_back_invalid()
        assert 'Введите корректный номер' in main_page.get_error_msg_text()

    def test_call_back_successful(self):
        main_page = Header()
        main_page.feedback()\
            .call_back_valid()\
            # .successfull_call_back()
        return main_page.successfull_call_back is True

    def test_placeholder(self):
        main_page = Header()
        main_page.is_placeholder_present()
        return True

    def test_search_results(self):
        main_page = Header()
        return main_page.check_search is True

    def test_invalid_search_results(self):
        pass

    