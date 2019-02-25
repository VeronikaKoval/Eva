import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

from selenium.webdriver.support import expected_conditions as EC


class Loginization(BasePage):

    # Locators

    login_btn_header = (By.CSS_SELECTOR, 'a.login-popup')
    login_popup = (By.CSS_SELECTOR, 'div[id="popup-modal"]')
    e_mail_field = (By.CSS_SELECTOR, 'input[name="login[username]"]')
    pass_field = (By.CSS_SELECTOR, 'input[name="login[password]"]')
    submit_btn = (By.CSS_SELECTOR, 'button[id="send2"]')
    personal_account_btn = (By.CSS_SELECTOR, 'span[data-bind="text customer().firstname"]')
    personal_account_popup = (By.CLASS_NAME, 'authorization-popup-list')

    authorization_pass_error = (By.CSS_SELECTOR, 'div.messages.fail')
    authorization_mail_error = (By.CSS_SELECTOR, 'div.mage-error')

    forgot_pass_btn = (By.CSS_SELECTOR, 'div.forgot-password')
    forgot_pass_popup = (By.CSS_SELECTOR, 'form.form-forgot-password')
    mail_field_in_forgot_pass = (By.CSS_SELECTOR, 'input#email_address')
    new_pass_btn = (By.CSS_SELECTOR, 'button.action.submit.primary')
    recovery_error_msg = (By.CSS_SELECTOR, 'div#email_address-error')
    recovery_pass_succ_msg = (By.CSS_SELECTOR, 'div.message-success')
    close_recovery_popup = (By.CSS_SELECTOR, 'button[data-role="closeBtn"]')

    # Axctions

    def is_login_popup_present(self):
        """ Checking presence of the login popup after clicking the login button"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        return self.is_element_present(self.login_popup)

    def authorize(self, login, password):
        """ Opening the login popup, entering the email and password"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        time.sleep(2)

        mail_field = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail_field.click()
        mail_field.send_keys(login)

        password_field = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password_field.click()
        password_field.send_keys(password)

        self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()
        # time.sleep(3)
        return self

    def get_account_name_text(self):
        """ Checking authorization with valid mail and valid password, :return:account name text"""
        return self.wait.until(EC.visibility_of_element_located(self.personal_account_btn)).text

    def get_error_text_wrong_email(self):
        """ Checking authorization with the invalid mail and valid password,
        :return: authorization error message text """
        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_error)).text

    def get_error_text_wrong_pass(self):
        """ Checking authorization with the valid mail and invalid password,
         :return: authorization error message text"""
        return self.wait.until(EC.visibility_of_element_located(self.authorization_pass_error)).text

    def recovery_password(self, email):
        """ Opening the login popup, clicking on "Забыли пароль" btn,
        entering email, clicking "Получить новый пароль" btn"""
        login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
        login.click()

        self.wait.until(EC.presence_of_element_located(self.forgot_pass_btn)).click()
        time.sleep(2)
        recovery_form = self.wait.until(EC.visibility_of_any_elements_located(self.mail_field_in_forgot_pass))[0]
        recovery_form.click()
        recovery_form.send_keys(email)
        self.wait.until(EC.visibility_of_any_elements_located(self.new_pass_btn))[0] \
            .click()

    def get_error_msg_recovery_wrong_email(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering invalid email(without "@"), :return: recovery error msg text """
        return self.wait.until(EC.visibility_of_element_located(self.recovery_error_msg)).text

    def get_recovery_success_msg_text(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering valid email, :return: recovery success msg text"""
        self.wait.until(EC.visibility_of_any_elements_located(self.close_recovery_popup))[0]\
            .click()
        return self.wait.until(EC.visibility_of_element_located(self.recovery_pass_succ_msg)).text