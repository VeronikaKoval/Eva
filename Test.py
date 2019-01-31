from selenium.common.exceptions import WebDriverException

from BaseTest import BaseTest

from MainPageHeader import Header

from Loginization import Loginization


class TestHeader(BaseTest):

    def test_confirm_location(self):
        """ Confirmation of the default location and verifying the text of the chose location """
        main_page = Header()
        main_page.confirm_default_location()
        assert 'Киев' in main_page.get_loc_text()

    def test_changing_lang(self):
        """ Changing the language of the site from RUS to UKR and verifying the changes """
        main_page = Header()
        main_page.change_language()
        assert 'ua/' in main_page.get_site_url()

    def test_change_location(self):
        """ Choosing the location from the drop down list """
        main_page = Header()
        assert 'ЛЬВОВ' in main_page.choose_location()

    def test_call_back_unsuccessful(self):
        """ Checking the call back with the invalid number and verifying the text of the error """
        main_page = Header()
        main_page.feedback()\
            .call_back_invalid()
        assert 'Введите корректный номер' in main_page.get_error_msg_text()

    def test_call_back_successful(self):
        """ Checking the call back with the valid number """
        main_page = Header()
        main_page.feedback()\
            .call_back_valid()
        assert main_page.successfull_call_back() is True

    def test_placeholder(self):
        """ Checking presence of the placeholder in the search field """
        main_page = Header()
        assert main_page.is_placeholder_present() is True

    def test_search_results(self):
        """ Testing search results with the valid query"""
        main_page = Header()
        assert main_page.check_search() is True

    def test_invalid_search_results(self):
        """ Testing search results with the invalid query and verifying the text of the error """
        main_page = Header()
        main_page.search_with_invalid_query()
        assert 'Извините, ничего не найдено для "xdcydcyu"' in main_page.get_error_msg_for_query()

    def test_login(self):
        """ Checking the pop up after clicking the login btn"""
        main_page = Loginization()
        assert main_page.login() is True

    def test_unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.unsuccessful_authorization_pass()

    def test_unsuccessful_authorization_mail(self):
        """ Checking authorization with the invalid mail and valid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.unsuccessful_authorization_email()

    def test_successful_authorization(self):
        """ Checking authorization with the valid email and password and verifying the name of the account of the
         registered person"""
        main_page = Loginization()
        assert 'Doctor' in main_page.get_account_text()

    def test_our_products(self):
        main_page = Header()
        assert main_page.our_products() is True

    def test_main_side_menu(self):
        main_page = Header()
        assert main_page.main_drop_down_menu() is True

    def test_hovering_menu_item(self):
        main_page = Header()
        assert main_page.hover_menu_items() is True

    def test_product_block(self):
        main_page = Header()
        assert main_page.product_block_is_present() is True

    # def test_product_item_elements(self):
    #     main_page = Header()
    #     assert main_page.check_elements_of_product_item() is True

    def test_linejka_tovarov_block(self):
        main_page = Header()
        assert main_page.check_linejka_tovarov() is True

    def test_naboru_block(self):
        main_page = Header()
        assert main_page.check_sets() is True

    def test_brands_block(self):
        main_page = Header()
        assert main_page.check_brands_block() is True

    def test_subscribe_unsuccessful(self):
        main_page = Header()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.subscribe_for_news_unsuccessful()

    def test_subscribe_successful(self):
        main_page = Header()
        assert 'Спасибо, что подписались на нашу рассылку.' in main_page.subscribe_for_news_successful()


