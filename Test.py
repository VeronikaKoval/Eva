from selenium.common.exceptions import WebDriverException

from BaseTest import BaseTest

from selenium.webdriver.common.by import By

from MainPageHeader import Header

from Loginization import Loginization


class TestHeader(BaseTest):

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
        main_page = Header()
        main_page.search_with_invalid_query()
        assert 'Извините, ничего не найдено для "xdcydcyu"' in main_page.get_error_msg_for_query()

    def test_login(self):
        main_page = Loginization()
        return main_page.login is True

    def test_unsuccessful_authorization_pass(self):
        main_page = Loginization()
        assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.unsuccessful_authorization_pass()

    def test_unsuccessful_authorization_mail(self):
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.unsuccessful_authorization_email()

    def test_successful_authorization(self):
        main_page = Loginization()
        assert 'Doctor' in main_page.get_account_text()

    def test_our_products(self):
        main_page = Header()
        main_page.our_products()

    def test_main_side_menu(self):
        main_page = Header()
        return main_page.main_drop_down_menu is True

    def test_hovering_menu_item(self):
        main_page = Header()
        main_page.hover_menu_items()
