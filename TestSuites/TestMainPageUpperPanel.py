from TestSuites.BaseTest import BaseTest

from Pages.MainPageUpperPanel import Panel


class TestPanel(BaseTest):

    def setup(self):
        super(TestPanel, self).setup()
        self.driver.get(self.base_url)

    def test_confirm_location(self):
        """ Confirmation of the suggested location 'Kyiv' and verifying the text of the chose location """
        panel = Panel()
        panel.confirm_default_location()
        assert 'Киев' in panel.get_loc_text(), 'The location is not Kyiv'

    def test_change_location(self):
        """ choosing 'Lviv' city as current city from the location drop-down list"""
        panel = Panel()
        panel.choose_location()
        assert 'ЛЬВОВ' in panel.get_loc_text_from_popup(), 'The location is not Lviv'

    def test_random_location(self):
        """ Clicking 'Choose another location' button, choosing random location from the list of location
        and verifying that popup with changed location is opened"""
        panel = Panel()
        assert panel.choose_random_loc() is True, 'The popup with new location is absent'

    def test_changing_lang(self):
        """ Changing the language of the site from RUS to UKR on the upper panel,
        :return: page current URL to verify that language has changed to URK """
        panel = Panel()
        panel.change_language()
        assert 'ua/' in panel.get_page_url(), 'ua/ is absent in the current page URl'

    def test_visibility_of_login_btn(self):
        panel = Panel()
        assert panel.is_login_btn_visible() is True, 'The login btn is not visible'

    def test_our_projects(self):
        """  Clicking on the 'Наши проекты' button on the upper panel, checking the presence of "Our projects" block"""
        panel = Panel()
        assert panel.is_our_projects_visible() is True, 'The "Наши проекты" block is not visible'

    def test_open_tabs_on_pannel(self):
        """ Clicking the "Stores" tab, then "News", "Help", "Certificate" tab on the upper panel,
         :return: page current URL to verify that URL is changed"""
        panel = Panel()
        assert '/stockists/' in panel.click_stores_tab(), '/stockists/ is absent in the current page URl'
        assert 'novosti' in panel.click_news_tab(),  'novosti is absent in the current page URl'
        assert panel.click_help_tab() is True, 'The "Help" popup is not visible'
        assert panel.click_certificate_tab() is True, 'The "Certificate" popup is not visible'