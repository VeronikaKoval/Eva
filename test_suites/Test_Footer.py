from base_components.BaseTest import BaseTest

from Pages.MainPageFooter import Footer


class TestFooter(BaseTest):

    def setup(self):
        super(TestFooter, self).setup()
        self.driver.get(self.base_url)

    def test_visibility_of_blocks(self):
        """
        Check if " Projects", "Help", " Hotline", "Subscribe" blocks in footer are visible
        """
        footer = Footer()
        assert footer.is_projects_visible() is True, 'Block "Projects" is not visible or absent'
        assert footer.is_help_visible() is True, 'Block "Help" is not visible or absent'
        assert footer.is_hotline_visible() is True, 'Block "Hot line" is not visible or absent'
        assert footer.is_subscribe_visible() is True, 'Block "Subscribe" is not visible or absent'
        assert footer.is_subscribe_field_visible() is True, '"Subscribe" field is not visible or absent'
        assert footer.is_subscribe_btn_visible() is True, '"Submit" btn is not visible or absent'
        assert footer.is_social_links_block_visible() is True, 'Block "Social links" is not visible or absent'

    def test_subscribe_unsuccessful(self):
        """
        Check the subscribe functionality with invalid email, get text of the error message
        """
        footer = Footer()
        footer.subscribe_for_news('ruzifawomaheximail.com')
        assert 'Пожалуйста, введите правильный адрес электронной почты' in footer.get_error_msg_text_newsletters(),\
            'The error message is different or absent'

    def test_subscribe_successful(self):
        """
        Check the subscribe functionality with valid email, get text of the success message
        """
        footer = Footer()
        footer.subscribe_for_news('baylan.oluwatimilehin@plutocow.com')
        assert 'Спасибо, что подписались на нашу рассылку.' in footer.get_success_msg_text_newsletters(), \
            'The success message is different or absent'

    def test_FB(self):
        """
        Clicking on Facebook link, verifying that it is opened in a new tab, checking page URL
        """
        footer = Footer()
        footer.click_FB()
        self.switch_to_previous_tab()
        # assert 'www.facebook.com/EVA.dp.ua' in footer.get_page_url(), 'URL doesnt match "facebook.com/EVA.dp.ua"'

    def test_youtube(self):
        """
        Click on Youtube link, verifying that it is opened in a new tab, checking page URL
        """
        footer = Footer()
        footer.click_youtube()
        self.switch_to_previous_tab()
        assert footer.get_page_url() == 'https://www.youtube.com/user/evadpua', \
            'URL doesnt match "youtube.com/user/evadpua"'

    def test_twitter(self):
        """
        Click on Twitter link, verifying that it is opened in a new tab, checking page URL
        """
        footer = Footer()
        footer.click_twitter()
        self.switch_to_previous_tab()
        assert footer.get_page_url() == 'https://twitter.com/eva__ua', 'URL doesnt match "twitter.com/eva__ua" '

    def test_instagram(self):
        """
        Click on Insagram link, verifying that it is opened in a new tab, checking page URL
        """
        footer = Footer()
        footer.click_instagram()
        self.switch_to_previous_tab()
        assert footer.get_page_url() == 'https://www.instagram.com/eva_ua/', 'URL doesnt match "instagram.com/eva_ua/" '
