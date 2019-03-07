import time

from TestSuites.BaseTest import BaseTest

from Pages.MainPageFooter import Footer


class TestFooter(BaseTest):

    def setup(self):
        super(TestFooter, self).setup()
        self.driver.get(self.base_url)

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
        # self.driver.window_handles()
        self.driver.switch_to.window(self.driver.window_handles[1])
        # time.sleep(2)
        assert 'plus.google.com/+EVAua500' in footer.get_page_url(), 'URL doesnt match "plus.google.com"'

    # def test_FB(self):
    #     """ Clicking on Facebook link, verifying that it is opened in a new tab, checking page URL"""
    #     footer = Footer()
    #     footer.click_FB()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     assert 'www.facebook.com/EVA.dp.ua' in footer.get_page_url(), 'URL doesnt match "facebook.com/EVA.dp.ua"'

    def test_youtube(self):
        """Clicking on Youtube link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_youtube()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert 'youtube.com/user/evadpua' in footer.get_page_url(), 'URL doesnt match "youtube.com/user/evadpua"'

    def test_twitter(self):
        """ Clicking on Twitter link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert 'twitter.com/eva__ua' in footer.get_page_url(), 'URL doesnt match "twitter.com/eva__ua" '

    # def test_viber(self):
    #     """ Clicking on Viber link, verifying that it is opened in a new tab, checking page URL"""
    #     footer = Footer()
    #     footer.click_viber()
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     assert 'chats.viber.com/evaua/en' in footer.get_page_url(), 'URL doesnt match'

    def test_instagram(self):
        """ Clicking on Insagram link, verifying that it is opened in a new tab, checking page URL"""
        footer = Footer()
        footer.click_instagram()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert 'instagram.com/eva_ua/' in footer.get_page_url(), 'URL doesnt match "instagram.com/eva_ua/" '

