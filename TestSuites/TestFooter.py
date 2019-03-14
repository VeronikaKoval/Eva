import time

from TestSuites.BaseTest import BaseTest

from Pages.MainPageFooter import Footer


class TestFooter(BaseTest):

    def setup(self):
        super(TestFooter, self).setup()
        self.driver.get(self.base_url)

    def test_visibility_of_blocks(self):
        """ Checking if all blocks in footer is visible, :return True if block is visible"""
        footer = Footer()
        assert footer.is_projects_visible() is True, 'Block "Projects" is not visible or absent'
        assert footer.is_help_visible() is True, 'Block "Help" is not visible or absent'
        assert footer.is_hotline_visible() is True, 'Block "Hot line" is not visible or absent'
        assert footer.is_subscribe_visible() is True, 'Block "Subscribe" is not visible or absent'
        assert footer.is_subscribe_field_visible() is True, '"Subscribe" field is not visible or absent'
        assert footer.is_subscribe_btn_visible() is True, '"Submit" btn is not visible or absent'
        assert footer.is_social_links_block_visible() is True, 'Block "Social links" is not visible or absent'


    def test_subscribe_unsuccessful(self):
        """ Clicking on the subscribe field, entering invalid email,
        :return: text of the error message to verify the error msg text """
        footer = Footer()
        footer.subscribe_for_news('ruzifawomaheximail.com')
        assert 'Пожалуйста, введите правильный адрес электронной почты' in footer.get_error_msg_text_newsletters(),\
            'The error message is different or absent'

    def test_subscribe_successful(self):
        """ Clicking on the subscribe field, entering valid email,
        :return: text of the success message to verify the success msg text"""
        footer = Footer()
        footer.subscribe_for_news('baylan.oluwatimilehin@plutocow.com')
        assert 'Спасибо, что подписались на нашу рассылку.' in footer.get_success_msg_text_newsletters(), \
            'The success message is different or absent'

    def test_open_Google(self):
        """ Clicking on Google link, verifying that it opens in a new tab, checking page URL"""
        footer = Footer()
        footer.click_Google()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert footer.get_page_url() == 'https://plus.google.com/+EVAua500', 'URL doesnt match "plus.google.com"'

    def test_FB(self):
        """ Clicking on Facebook link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_FB()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # assert 'www.facebook.com/EVA.dp.ua' in footer.get_page_url(), 'URL doesnt match "facebook.com/EVA.dp.ua"'

    def test_youtube(self):
        """Clicking on Youtube link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_youtube()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert footer.get_page_url() == 'https://www.youtube.com/user/evadpua', \
            'URL doesnt match "youtube.com/user/evadpua"'

    def test_twitter(self):
        """ Clicking on Twitter link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert footer.get_page_url() == 'https://twitter.com/eva__ua', 'URL doesnt match "twitter.com/eva__ua" '

    def test_instagram(self):
        """ Clicking on Insagram link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_instagram()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert footer.get_page_url() == 'https://www.instagram.com/eva_ua/', 'URL doesnt match "instagram.com/eva_ua/" '
