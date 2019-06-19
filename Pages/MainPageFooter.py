from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_components.BasePage import BasePage


class Footer(BasePage):

    #Locators

    subscribe_field = (By.CSS_SELECTOR, 'input#newsletter')
    subscribe_btn = (By.CSS_SELECTOR, 'button[title="Подписаться"]')
    subscription_error = (By.CSS_SELECTOR, 'div#newsletter-error')
    subscription_success = (By.CSS_SELECTOR, 'div.page.messages')

    social_links_block = (By.CSS_SELECTOR, 'div.social-icons')

    Google_link = (By.CSS_SELECTOR, 'a[href="https://plus.google.com/+EVAua500"]')
    FB_link = (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/EVA.dp.ua"]')
    Youtube_link = (By.CSS_SELECTOR, 'a[href="https://www.youtube.com/user/evadpua"]')
    Twitter_link = (By.CSS_SELECTOR, 'a[href="https://twitter.com/eva__ua"]')
    Viber_link = (By.CSS_SELECTOR, 'a[href="https://chats.viber.com/evaua"]')
    Insta_link = (By.CSS_SELECTOR, 'a[href="https://www.instagram.com/eva_ua/"]')

    block_projects = (By.CSS_SELECTOR, 'div.footer-block.projects')
    block_help = (By.CSS_SELECTOR, 'div.footer-block.help')
    block_hotline = (By.CSS_SELECTOR, 'div.footer-block.hotline')
    block_subsribe = (By.CSS_SELECTOR, 'div.footer-block.subscribe')

    bottom_logo = (By.CSS_SELECTOR, 'div.bottom-logo')

    #Actions

    def subscribe_for_news(self, email):
        """
        Click on the subscribe field, entering email, clicking "Subscribe" btn,
        :return: object of page
        """
        subscribe = self.wait.until(EC.visibility_of_element_located(self.subscribe_field))
        subscribe.click()
        subscribe.send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.subscribe_btn)).click()
        return self

    def get_error_msg_text_newsletters(self):
        """
        Get error message text after subscribing for news with invalid email,
         :return: text of the error message
         """
        return self.wait.until(EC.visibility_of_element_located(self.subscription_error)).text

    def get_success_msg_text_newsletters(self):
        """
        Get error message text after subscribing for news with valid email,
        :return: text of the success message
        """
        return self.wait.until(EC.visibility_of_element_located(self.subscription_success)).text

    def click_social_media_link(self, locator):
        """
        Click on social link in footer,
        :return: object of page
        """
        return self.wait.until(EC.visibility_of_element_located(locator)).click()

    def click_Google(self):
        """
        Click on Google link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.Google_link)

    def click_FB(self):
        """
        Click on Facebook link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.FB_link)

    def click_youtube(self):
        """ Click on Youtube link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.Youtube_link)

    def click_twitter(self):
        """
        Click on Twitter link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.Twitter_link)

    def click_viber(self):
        """
        Click on Viber link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.Viber_link)

    def click_instagram(self):
        """
        Click on Instagram link, verifying that it is opened in a new tab,
        :return: object of page
        """
        return self.click_social_media_link(self.Insta_link)

    def is_projects_visible(self):
        """ Check if block "Projects" is visible,
        :return: True if element is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.block_projects, 'НАШИ ПРОЕКТЫ')

    def is_help_visible(self):
        """  Check if block "Help" is visible,
        :return: True if element is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.block_help, 'ПОМОЩЬ')

    def is_hotline_visible(self):
        """  Check if block "Hot line" is visible,
        :return: True if element is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.block_hotline, 'ГОРЯЧАЯ ЛИНИЯ')

    def is_subscribe_visible(self):
        """  Check if block "Subscribe" is visible,
        :return: True if element is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.block_subsribe, 'ПОДПИСКА НА НОВОСТИ')

    def is_subscribe_field_visible(self):
        """ Check if the "Subscribe" field is visible,
        :return: True if field is visible, otherwise returns 'False'
        """
        return self.is_element_present(self.subscribe_field, 'Subscribe field')

    def is_subscribe_btn_visible(self):
        """
        Check the "Submit" btn in the subscribe block is visible,
        :return: True if button is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.subscribe_btn, 'Subscribe button')

    def is_social_links_block_visible(self):
        """
        Check the "Social links" block is visible,
        :return: True if block is visible
        """
        return self.is_element_visible(self.social_links_block, 'СОЦИАЛЬНЫЕ СЕТИ')

    def is_bottom_logo_visible(self):
        """
        Check if the bottom logo is visible,
        :return True if logo is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.bottom_logo, 'logo')
