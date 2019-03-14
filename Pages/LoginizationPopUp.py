import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage

from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePopUp import BasePopup
from Pages.RecoveryPassPopUp import RecoveryPassPopUp


class LoginPopup(BasePage):

    # Locators

    popup_locator = (By.CSS_SELECTOR, 'div[id="popup-modal"]')

    login_btn_header = (By.CSS_SELECTOR, 'a.login-popup')
    e_mail_field = (By.CSS_SELECTOR, 'input[name="login[username]"]')
    pass_field = (By.CSS_SELECTOR, 'input[name="login[password]"]')
    submit_btn = (By.CSS_SELECTOR, 'button[id="send2"]')
    checkbox_stay_on_site = (By.CSS_SELECTOR, 'input#stayon')

    personal_account_btn = (By.CSS_SELECTOR, 'a.js-authorization-account-popup.show-desktop')
    personal_account_popup = (By.CLASS_NAME, 'authorization-popup-list')
    register_link = (By.CSS_SELECTOR, 'div.login-bottom-link__registration')

    authorization_pass_error = (By.CSS_SELECTOR, 'div.messages.fail')
    authorization_mail_error = (By.CSS_SELECTOR, 'div.mage-error')
    authorization_mail_and_pass_error = (By.CSS_SELECTOR, 'div#email-error')

    forgot_pass_btn = (By.CSS_SELECTOR, 'div.forgot-password')

    # close_popup_btn = (By.CSS_SELECTOR, 'button[data-role="closeBtn"]')
    close_popup_btn = (By.XPATH, '/html/body/div[3]/aside[1]/div[2]/header/button')

    recovery_pass_succ_msg = (By.CSS_SELECTOR, 'div.message-success.success.message') #(By.CSS_SELECTOR, 'div[data-placeholder="messages"]') #(By.CSS_SELECTOR, 'div.message-success')

    # Actions

    def __init__(self):
        super(LoginPopup, self).__init__()
        popup_window = self.wait.until(EC.visibility_of_element_located(self.popup_locator))
        self.wait = WebDriverWait(popup_window, self.wait_element_time)

    def is_login_popup_visible(self):
        """ Checking presence of the login popup after clicking the login button,
         :return: True if Login popup is visible """
        return self.is_element_visible(self.popup_locator)

    def is_register_link_visible(self):
        """ Checking if the register link visible in the login popup,
        :return: True if "Register" link is visible in login popup"""
        return self.is_element_visible(self.register_link)

    def is_forgot_pass_link_visible(self):
        """ Checking if the "Forgot password" link visible in the login popup,
        :return: True if "Forgot password" link is visible in login popup"""
        return self.is_element_visible(self.forgot_pass_btn)

    def is_email_field_visible(self):
        """ Checking if the email field is visible in the login popup,
        :return: True if email field is visible"""
        return self.is_element_visible(self.e_mail_field)

    def is_pass_field_visible(self):
        """ Checking if the password field is visible in the login popup,
        :return: True if password field is visible"""
        return self.is_element_visible(self.pass_field)

    def is_submit_btn_visible(self):
        """ Checking if the "Submit" button is visible in the login popup,
        :return: True if "Submit" button is visible"""
        return self.is_element_visible(self.submit_btn)

    def is_checkbox_visible(self):
        """ Checking if the "Stay on site" checkbox is visible in the login popup,
        :return: True if "Stay on site" checkbox is visible """
        return self.is_element_visible(self.checkbox_stay_on_site)

    def authorize(self, login, password):
        """ Opening the login popup, entering the email and password, clicking "Submit" btn,
        :return: object of page"""
        mail_field = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail_field.click()
        mail_field.send_keys(login)
        time.sleep(1.5)

        password_field = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password_field.click()
        password_field.send_keys(password)
        time.sleep(1.5)

        self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()
        return self

    def is_popup_present_after_authorization(self):
        """ Clicking on the personal account btn after authorization, checking if the popup visible,
        :return: True, if a popup visible after clicking in your account btn"""
        self.wait.until(EC.presence_of_element_located(self.personal_account_btn)).click()
        time.sleep(1)
        return self.is_element_visible(self.personal_account_popup)

    def get_error_text_wrong_email(self):
        """ Checking authorization with the invalid mail and valid password,
        :return: authorization error message text """
        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_error)).text

    def get_error_text_wrong_pass(self):
        """ Checking authorization with the valid mail and invalid password,
         :return: authorization error message text"""
        return self.wait.until(EC.visibility_of_element_located(self.authorization_pass_error)).text

    def authorization_with_empty_field(self):
        """ Clicking the submit button, without entering login and password,
        :return: object of page"""
        return self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()

    def get_error_text_with_empty_login_pass(self):
        """ Checking authorization with the empty mail and invalid password,
         :return: authorization error message text"""
        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_and_pass_error)).text

    def close_login_popup(self):
        """ Clicking "Close" btn to close login popup,
        :return: object of page """
        self.wait.until(EC.visibility_of_element_located(self.close_popup_btn)).click()
        return self

    def click_forgot_pass(self):
        """ Clicking on the "Forgot password" button, trying to find element for the second time if the 1st click
        failed, :return: object: RecoveryPassPopUp"""
        btn = self.wait.until(EC.element_to_be_clickable(self.forgot_pass_btn))
        btn.click()
        # time.sleep(0.2)
        try:
            popup_window = WebDriverWait(self.driver, 1).until(EC.visibility_of_any_elements_located(RecoveryPassPopUp.popup_locator))[0]
        except:
            print('click')
            btn.click()

        return RecoveryPassPopUp()
