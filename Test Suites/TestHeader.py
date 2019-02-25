from BaseTest import BaseTest

from Pages.MainPageHeader import Header


class TestHeader(BaseTest):

    def test_confirm_location(self):
        """ Confirmation of the suggested location 'Kyiv' and verifying the text of the chose location """
        main_page = Header()
        main_page.confirm_default_location()
        assert 'Киев' in main_page.get_loc_text()

    def test_change_location(self):
        """ choosing 'Lviv' city as current city from the location drop-down list"""
        main_page = Header()
        main_page.choose_location()
        assert 'ЛЬВОВ' in main_page.get_loc_text_from_popup()

    def test_random_location(self):
        """ Clicking 'Choose another location' button, choosing random location from the list of location
        and verifying that popup with changed location is opened"""
        main_page = Header()
        assert main_page.choose_random_loc(), 'Popup is absent' is True

    def test_changing_lang(self):
        """ Changing the language of the site from RUS to UKR on the upper panel,
        :return: page current URL to verify that language has changed to URK """
        main_page = Header()
        main_page.change_language()
        assert 'ua/', 'ua/ is absent in the current page URl' in main_page.get_page_url()

    def test_call_back_unsuccessful(self):
        """ Clicking on feedback link to get feedback pop up, clicking on the phone field,
        entering invalid phone number, :return: text of the error message"""
        main_page = Header()
        main_page.call_back(phone_number='00000000')
        assert 'Введите корректный номер', \
            'The text of the error is absent' in main_page.get_error_text_with_invalid_number()

    def test_call_back_successful(self):
        """ Clicking on feedback link to get feedback pop up, clicking on the phone field,
                entering valid phone number, :return: text of the success message"""
        main_page = Header()
        main_page.call_back(phone_number='123456789')
        assert 'СПАСИБО ЗА ОБРАЩЕНИЕ!'\
            , 'The success message is absent' in main_page.get_successful_msg_text_with_valid_number()

    def test_search_field(self):
        """ Checking presence of the placeholder in the search field """
        main_page = Header()
        assert main_page.is_search_field_present() is True

    def test_search_results_block(self):
        """  Clicking on the search field, entering valid search query "духи"
        and checking whether the block with search results is present """
        main_page = Header()
        main_page.enter_query_into_seqrch_field('духи')
        assert main_page.is_search_result_block_present() is True

    def test_invalid_search_results(self):
        """ Clicking on the search field, entering invalid search query,
        :return: text of the error for the invalid query to verify the text of the error """
        main_page = Header()
        main_page.enter_query_into_seqrch_field('xdcydcyu')
        assert 'Извините, ничего не найдено для "xdcydcyu"' in main_page.get_error_msg_for_invalid_query()

    def test_our_projects(self):
        """  Clicking on the 'Наши проекты' button on the upper panel, checking the presence of "Our projects" block"""
        main_page = Header()
        assert main_page.is_our_projects_present() is True

    def test_main_drop_down_menu(self):
        """ Clicking on 'Все разделы' menu item, checking the presence of the side drop down menu"""
        main_page = Header()
        assert main_page.is_main_drop_down_menu_present() is True

    # def test_hovering_menu_item(self):
    #     """ Hovering main menu items"""
    #     main_page = Header()
    #     assert main_page.hover_menu_items() is True

    def test_presence_of_presence_of_all_blocks(self):
        """ Checking if the "Product block", "Linejka tovarov", "Nabory", "Brands" are present """
        main_page = Header()
        assert main_page.is_pokupajte_vigodno_present() is True
        assert main_page.is_linejka_tovarov_present() is True
        assert main_page.is_nabory_present() is True
        assert main_page.is_brands_block_present() is True

    def test_subscribe_unsuccessful(self):
        """ Clicking on the subscribe field, entering invalid email,
        :return: text of the error message to verify the error msg text """
        main_page = Header()
        main_page.subscribe_for_news('ruzifawomaheximail.com')
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_msg_text_newsletters()

    def test_subscribe_successful(self):
        """ Clicking on the subscribe field, entering valid email,
         :return: text of the success message to verify the success msg text"""
        main_page = Header()
        main_page.subscribe_for_news('baylan.oluwatimilehin@plutocow.com')
        assert 'Спасибо, что подписались на нашу рассылку.' in main_page.get_success_msg_text_newsletters()

    def test_open_tabs_on_pannel(self):
        """ Clicking the "Stores" tab, then "News" tabon the upper panel,
         :return: page current URL to verify that URL is changed"""
        main_page = Header()
        assert '/stockists/' in main_page.click_stores_tab()
        assert 'novosti' in main_page.click_news_tab()
        assert main_page.click_help_tab() is True
        assert main_page.click_certificate_tab() is True

    def test_wishlist(self):
        """ Opening the 'Wishlist' and verifying that it isn't available for unregistered account """
        main_page = Header()
        assert '#account_login' in main_page.checking_wishlist()

    def test_cart(self):
        """ Opening the 'Cart' and verifying that it isn't available for unregistered account"""
        main_page = Header()
        assert main_page.checking_cart() is True

    def test_logo(self):
        """ Opening the "Uhod" tab, clicking on the logo to verify that it returns to the main page"""
        main_page = Header()
        assert 'https://eva.ua/024/uhod-soboj/' not in main_page.checking_logo()