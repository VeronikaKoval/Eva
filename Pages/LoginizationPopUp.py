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

    personal_account_btn = (By.CSS_SELECTOR, 'a.js-authorization-account-popup.show-desktop') #(By.CSS_SELECTOR, 'div#ui-id-10') #(By.CSS_SELECTOR, 'span[data-bind="text customer().firstname"]')
    personal_account_popup = (By.CLASS_NAME, 'authorization-popup-list')
    register_link = (By.CSS_SELECTOR, 'div.login-bottom-link__registration')

    authorization_pass_error = (By.CSS_SELECTOR, 'div.messages.fail')
    authorization_mail_error = (By.CSS_SELECTOR, 'div.mage-error')
    authorization_mail_and_pass_error = (By.CSS_SELECTOR, 'div#email-error')

    forgot_pass_btn = (By.CSS_SELECTOR, 'div.forgot-password')

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

    def authorize(self, login, password):
        """ Opening the login popup, entering the email and password"""
        mail_field = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail_field.click()
        mail_field.send_keys(login)
        time.sleep(1)

        password_field = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password_field.click()
        password_field.send_keys(password)

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
        """ Clicking the submit button, without entering login and password"""
        return self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()
        # return self

    def get_error_text_with_empty_login_pass(self):
        """ Checking authorization with the empty mail and invalid password,
         :return: authorization error message text"""
        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_and_pass_error)).text

    def click_forgot_pass(self):
        """ Clicking on the "Forgot password" button, trying to find element for the second time if the 1st click
        failed"""
        btn = self.wait.until(EC.element_to_be_clickable(self.forgot_pass_btn))
        btn.click()
        # time.sleep(0.2)
        try:
            popup_window = WebDriverWait(self.driver, 1).until(EC.visibility_of_any_elements_located(RecoveryPassPopUp.popup_locator))[0]
        except:
            print('click')
            btn.click()

        return RecoveryPassPopUp()



# class RecoveryPassPopUp(LoginPopup):
#
#     recover_locator = (By.CSS_SELECTOR, 'form.form-forgot-password')
#
#     def __init__(self):
#         super(RecoveryPassPopUp, self).__init__()
#         recover_window = self.wait.until(EC.visibility_of_element_located(self.recover_locator))
#         self.wait = WebDriverWait(recover_window, self.wait_element_time)
