import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePopUp import BasePopup


class RecoveryPassPopUp(BasePopup):

    # Locators

    popup_locator = (By.CSS_SELECTOR, 'form.form-forgot-password')

    recovery_error_msg = (By.CSS_SELECTOR, 'div#email_address-error')
    mail_field_in_recovery = (By.CSS_SELECTOR, 'input#email_address')  #(By.CSS_SELECTOR, 'input[alt="email"]')
    new_pass_btn = (By.CSS_SELECTOR, 'button.action.submit.primary')
    close_recovery_popup_btn = (By.CSS_SELECTOR, 'button[data-role="closeBtn"]')
    recovery_pass_succ_msg = (By.CSS_SELECTOR, 'div.message-success')


    def recovery(self, mail):
        """ Entering email, clicking "Получить новый пароль" btn"""
        enter_mail = self.wait.until(EC.visibility_of_element_located(self.mail_field_in_recovery))
        enter_mail.send_keys(mail)
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.new_pass_btn)).click()
        return self

    def get_error_msg_recovery_wrong_email(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering invalid email(without "@"), :return: recovery error msg text """
        return self.wait.until(EC.visibility_of_element_located(self.recovery_error_msg)).text

    def close_login_popup(self):
        """ Clicking "Close" btn to close login popup"""
        self.wait.until(EC.visibility_of_any_elements_located(self.close_recovery_popup_btn)).click()
        return self

    def get_recovery_success_msg_text(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering valid email,
        clicking "Получить новый пароль" btn", :return: recovery success msg text"""
        return self.wait.until(EC.visibility_of_element_located(self.recovery_pass_succ_msg)).text
