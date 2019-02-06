import time

from selenium.webdriver.common.by import By

from BasePage import BasePage

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
    recovery_pass_succ_msg = (By.CSS_SELECTOR, 'div.message-success') #(By.CSS_SELECTOR, 'div.page messages')
    close_recovery_popup = (By.CSS_SELECTOR, 'button[data-role="closeBtn"]') #(By.XPATH, '//aside[contains(@class,"_inner-scroll _show")]//button[contains(@type,"button")]')


    # Axctions

    def login(self):
        """ Checking presence the login popup after clicking the login button"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        try:
            self.wait.until(EC.visibility_of_element_located(self.login_popup))
            return True
        except:
            return False

    def authorize(self, login, password):
        """ Opening the popup, entering the email and password"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        time.sleep(2)

        mail_field = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail_field.click()
        mail_field.send_keys(login)

        password_field = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password_field.click()
        password_field.send_keys(password)

        self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()
        time.sleep(3)

    def get_account_text(self):
        """ Checking authorization with valid mail and valid password and returning account name"""
        self.authorize(login='ruzifawoma@heximail.com', password='qi3R8Ue4gj8g9BV')
        return self.wait.until(EC.visibility_of_element_located(self.personal_account_btn)).text

    def unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password and returning text of the error message"""
        self.authorize(login='ruzifawoma@heximail.com', password='chcciicnbcg')
        return self.wait.until(EC.visibility_of_element_located(self.authorization_pass_error)).text

    def unsuccessful_authorization_email(self):
        """ Checking authorization with the invalid mail and valid password and returning text of the error message"""
        self.authorize(login='ruzifawoma@heximailcom', password='qi3R8Ue4gj8g9BV')
        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_error)).text

    def recovery_password(self, email):
        """ Checking recovery of the password """
        login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
        login.click()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located(self.forgot_pass_btn)).click()
        time.sleep(2)
        recovery_form = self.wait.until(EC.visibility_of_any_elements_located(self.mail_field_in_forgot_pass))[0]
        recovery_form.click()
        recovery_form.send_keys(email)
        self.wait.until(EC.visibility_of_any_elements_located(self.new_pass_btn))[0] \
            .click()

    def recovery_pass_unsuccess(self):
        """ Checking recovery of the password with the invalid email"""
        self.recovery_password(email='qevawenemmo-7199yopmail.com')
        return self.wait.until(EC.visibility_of_element_located(self.recovery_error_msg)).text

    def recovery_pass_success(self):
        """ Checking recovery of the password with the valid email"""
        self.recovery_password(email='cemmozosyh-0165@yopmail.com')
        self.wait.until(EC.visibility_of_any_elements_located(self.close_recovery_popup))[0]\
            .click()
        return self.wait.until(EC.visibility_of_element_located(self.recovery_pass_succ_msg)).text