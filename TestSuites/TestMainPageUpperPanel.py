import time

from Pages.MainPageBody import Body
from TestSuites.BaseTest import BaseTest

from Pages.MainPageUpperPanel import Panel


class TestPanel(BaseTest):

    def setup(self):
        super(TestPanel, self).setup()
        self.driver.get(self.base_url)

    def test_confirm_location(self):
        """ Clicking "Confirm loc" btn on the suggested location 'Kyiv' and verifying the text of the chosen location"""
        panel = Panel()
        assert panel.is_confirm_loc_btn_visible() is True, '"Confirm location" btn is not visible'
        panel.click_confirm_suggested_location()
        assert 'Киев' in panel.get_loc_text(), 'The location is not Kyiv'

    def test_change_location(self):
        """ Choosing 'Lviv' city as current city from the location drop-down list"""
        panel = Panel()
        panel.choose_location()
        assert 'ЛЬВОВ' in panel.get_loc_text_from_popup(), 'The location is not Lviv'

    def test_random_location(self):
        """ Clicking 'Choose another location' button, choosing random location from the list of location
        and verifying that popup with changed location is opened"""
        panel = Panel()
        panel.choose_random_loc()
        assert panel.is_location_changed_popup_visible() is True, 'The popup with new location is not visible or absent'
        self.save_screenshot('screen_location.png')

    def test_changing_lang(self):
        """ Changing the language of the site from RUS to UKR on the upper panel, getting page URL to verify that
        language has changed to URK """
        panel = Panel()
        panel.change_language()
        time.sleep(1)
        assert 'ua/' in panel.get_page_url(), 'ua/ is absent in the current page URl'

    def test_adding_language_cookie(self):
        """ Adding cookies, which are responsible for UKR language, getting page URL to verify that
        language has changed to URK """
        panel = Panel()
        panel.add_lang_cookies()
        time.sleep(1)
        assert 'ua/' in panel.get_page_url(), 'ua/ is absent in the current page URl'

    def test_visibility_of_login_btn(self):
        """ Checking if the login button is visible """
        panel = Panel()
        assert panel.is_login_btn_visible() is True, 'The login btn is not visible'

    def test_our_projects(self):
        """  Clicking on the 'Наши проекты' button on the upper panel, checking the presence and
        visibility of "Our projects" block """
        panel = Panel()
        assert panel.is_our_projects_visible() is True, 'The "Наши проекты" block is not visible'

    def test_click_tabs_on_pannel(self):
        """ Clicking the "Stores", then "News", tab on the upper panel, getting page current
        URL to check that page has opened and Url changed """
        panel = Panel()
        panel.click_stores_tab()
        main_page = Body()
        assert '/stockists/' in main_page.get_page_url(), '/stockists/ is absent in the current page URl'
        panel.click_news_tab()
        assert 'novosti' in main_page.get_page_url(),  'novosti is absent in the current page URl'

    def test_open_tabs_on_panel(self):
        """ Clicking the "Help" and then "Certificate" tab on the upper panel to check whether the popup is opened
        and visible"""
        panel = Panel()
        assert panel.click_help_tab() is True, 'The "Help" popup is not visible'
        assert panel.click_certificate_tab() is True, 'The "Certificate" popup is not visible'