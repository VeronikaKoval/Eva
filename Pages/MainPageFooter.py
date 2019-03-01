import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class Footer(BasePage):

    #Locators

    subscribe_field = (By.CSS_SELECTOR, 'input#newsletter')
    subscribe_btn = (By.CSS_SELECTOR, 'button[title="Подписаться"]')
    subscription_error = (By.CSS_SELECTOR, 'div#newsletter-error')
    subscription_success = (By.CSS_SELECTOR, 'div.page.messages')

    social_links_block = (By.CSS_SELECTOR, 'div.social-icons')
    each_social_link = (By. CSS_SELECTOR, 'a.icon-link')

    Google_link = (By.CSS_SELECTOR, 'a[href="https://plus.google.com/+EVAua500"]')
    FB_link = (By.CSS_SELECTOR, 'a[href="https://www.facebook.com/EVA.dp.ua"]')
    Youtube_link = (By.CSS_SELECTOR, 'a[href="https://www.youtube.com/user/evadpua"]')
    Twitter_link = (By.CSS_SELECTOR, 'a[href="https://twitter.com/eva__ua"]')
    Viber_link = (By.CSS_SELECTOR, 'a[href="https://chats.viber.com/evaua"]')
    Insta_link = (By.CSS_SELECTOR, 'a[href="https://www.instagram.com/eva_ua/"]')


    #Actions

    def subscribe_for_news(self, email):
        """ Clicking on the subscribe field, entering email"""
        subscribe = self.wait.until(EC.visibility_of_element_located(self.subscribe_field))
        subscribe.click()
        subscribe.send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.subscribe_btn)).click()
        return self

    def get_error_msg_text_newsletters(self):
        """ Getting error message text after subscribing for news with invalid email,
         :return: text of the error message"""
        return self.wait.until(EC.visibility_of_element_located(self.subscription_error)).text

    def get_success_msg_text_newsletters(self):
        """ Getting error message text after subscribing for news with valid email,
        :return: text of the success message"""
        return self.wait.until(EC.visibility_of_element_located(self.subscription_success)).text

    def click_social_media_link(self, locator):
        """ Clicking on social link in footer"""
        self.wait.until(EC.visibility_of_element_located(locator)).click()
        return self

    def click_Google(self):
        """ Clicking on Google link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.Google_link)

    def click_FB(self):
        """ Clicking on Facebook link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.FB_link)

    def click_youtube(self):
        """ Clicking on Youtube link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.Youtube_link)

    def click_twitter(self):
        """ Clicking on Twitter link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.Twitter_link)

    def click_viber(self):
        """ Clicking on Viber link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.Viber_link)

    def click_instagram(self):
        """ Clicking on Instagram link, verifying that it is opened in a new tab"""
        return self.click_social_media_link(self.Insta_link)

    def get_page_url(self):
        """ Getting the page url, :return: page current URL"""
        return self.driver.current_url
