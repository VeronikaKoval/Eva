import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_components.BasePopUp import BasePopup


class RecoveryPassPopUp(BasePopup):

    # Locators

    popup_locator = (By.CSS_SELECTOR, 'form.form-forgot-password')

    recovery_error_msg = (By.CSS_SELECTOR, 'div#email_address-error')
    mail_field_in_recovery = (By.CSS_SELECTOR, 'input#email_address')
    new_pass_btn = (By.CSS_SELECTOR, 'button.action.submit.primary')

    def recovery(self, mail):
        """
        Enter email, clicking "Получить новый пароль" btn
        :return: object of page
        """
        enter_mail = self.wait.until(EC.visibility_of_element_located(self.mail_field_in_recovery))
        enter_mail.send_keys(mail)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.new_pass_btn)).click()
        return self

    def get_error_msg_recovery_wrong_email(self):
        """
        Open the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering invalid email(without "@"),
        :return: recovery error msg text
        """
        return self.wait.until(EC.visibility_of_element_located(self.recovery_error_msg)).text

    def is_get_new_pass_btn_visible(self):
        """
        Check if the "Get new pass" btn is visible,
        :return: True, if button is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.new_pass_btn, 'Get new pass button')

    def is_mail_in_recovery_visible(self):
        """
        Check if the email field is visible,
        :return: True, if field is visible, otherwise returns 'False'
        """
        return self.is_element_visible(self.mail_field_in_recovery, 'Mail field in recovery password')