from TestSuites.BaseTest import BaseTest

from Pages.MainPageHeader import Header


class TestHeader(BaseTest):

    def setup(self):
        super(TestHeader, self).setup()
        self.driver.get(self.base_url)

    def test_call_back_unsuccessful(self):
        """ Clicking on feedback link to get feedback pop up, clicking on the phone field,
        entering invalid phone number, :return: text of the error message"""
        main_page = Header()
        main_page.call_back(phone_number='00000000')
        assert 'Введите корректный номер' in main_page.get_error_text_with_invalid_number(), \
            'The text of the error is absent'

    def test_call_back_successful(self):
        """ Clicking on feedback link to get feedback pop up, clicking on the phone field,
                entering valid phone number, :return: text of the success message"""
        main_page = Header()
        main_page.call_back(phone_number='123456789')
        assert 'СПАСИБО ЗА ОБРАЩЕНИЕ!' in main_page.get_successful_msg_text_with_valid_number(), \
            'The success message is absent'

    def test_search_field(self):
        """ Checking presence of the search field """
        main_page = Header()
        assert main_page.is_search_field_visible() is True, 'The search field is not visible'

    def test_search_results_block(self):
        """  Clicking on the search field, entering valid search query "духи"
        and checking whether the block with search results is present """
        main_page = Header()
        main_page.enter_query_into_search_field('духи')
        assert main_page.is_search_result_block_present() is True, 'The search result block is absent for a valid query'

    def test_invalid_search_results(self):
        """ Clicking on the search field, entering invalid search query,
        :return: text of the error for the invalid query to verify the text of the error """
        main_page = Header()
        main_page.enter_query_into_search_field('xdcydcyu')
        assert 'Извините, ничего не найдено для "xdcydcyu"' in main_page.get_error_msg_for_invalid_query(), \
            'The error message for invalid query is absent'

    def test_open_wishlist(self):
        """ Opening the 'Wishlist' as unregistered user, verifying that login popup is opened
        and it is empty for unregistered user """
        main_page = Header()
        main_page.open_wishlist()
        assert 'account_login' in main_page.get_page_url(), 'URL is different'

    def test_open_cart(self):
        """ Opening the 'Cart', verifying that cart popup is opened and it is empty for unregistered account"""
        main_page = Header()
        assert main_page.open_cart() is True, 'The cart popup is not visible'
        assert 'ВАША КОРЗИНА ПУСТА!' in main_page.get_text_from_cart_popup(), 'The text in the popup is different'

    def test_logo(self):
        """ Opening the "Uhod" tab, clicking on the logo to verify that it returns to the main page"""
        main_page = Header()
        main_page.click_logo()
        assert main_page.is_logo_visible() is True, 'Logo is not visible'
        assert 'uhod-soboj/' not in main_page.get_page_url(), 'URL is different'

