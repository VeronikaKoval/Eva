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
    # personal_account_popup = (By.CSS_SELECTOR, 'ul.authorization-popup-list')
    personal_account_popup = (By.CLASS_NAME, 'authorization-popup-list')

    authorization_pass_error = (By.CSS_SELECTOR, 'div.messages.fail')
    authorization_mail_error = (By.CSS_SELECTOR, 'div.mage-error')

    forgot_pass_btn = (By.CSS_SELECTOR, 'div.forgot-password')
    forgot_pass_popup = (By.CSS_SELECTOR, 'form.form-forgot-password')
    mail_field_in_forgot_pass = (By.XPATH, '//div[@class="field email required"]//input[@name="email"]')
    new_pass_btn = (By.XPATH, '//form[@id="form-validate"]//button[@type="submit"]')
    recovery_pass_succ_msg = (By.CSS_SELECTOR, 'div.page messages')
    close_recovery_popup = (By.XPATH, '//aside[contains(@class,"_inner-scroll _show")]//button[contains(@type,"button")]')


    # Axctions

    def login(self):
        """ Checking login popup after clicking the login button"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        try:
            self.wait.until(EC.visibility_of_element_located(self.login_popup))
            return True
        except:
            return False

    # def successful_authorization(self):
    #     """ Checking authorization with valid login and pass(through personal account popup)"""
    #     login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
    #     login.click()
    #     time.sleep(3)

    #     mail = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
    #     mail.click()
    #     mail.send_keys('ruzifawoma@heximail.com')

    #     password = self.wait.until(EC.presence_of_element_located(self.pass_field))
    #     password.click()
    #     password.send_keys('qi3R8Ue4gj8g9BV')

    #     submit = self.wait.until(EC.visibility_of_element_located(self.submit_btn))
    #     submit.click()
    #     time.sleep(3)
    #
    #     personal_acc = self.wait.until(EC.visibility_of_element_located(self.personal_account_btn))
    #     personal_acc.click()
    #     time.sleep(3)
    #     try:
    #         self.wait.until(EC.visibility_of_element_located(self.personal_account_popup))
    #         return True
    #     except:
    #         return False

    def get_account_text(self):
        """ Checking authorization with valid mail and valid password"""
        self.wait.until(EC.presence_of_element_located(self.login_btn_header)).click()
        time.sleep(2)

        mail = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail.click()
        mail.send_keys('ruzifawoma@heximail.com')

        password = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password.click()
        password.send_keys('qi3R8Ue4gj8g9BV')

        self.wait.until(EC.visibility_of_element_located(self.submit_btn)).click()
        time.sleep(3)

        return self.wait.until(EC.visibility_of_element_located(self.personal_account_btn)).text

    def unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password"""
        login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
        login.click()
        time.sleep(2)

        mail = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail.click()
        mail.send_keys('ruzifawoma@heximail.com')

        password = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password.click()
        password.send_keys('chcciicnbcg')

        submit = self.wait.until(EC.visibility_of_element_located(self.submit_btn))
        submit.click()
        time.sleep(3)

        return self.wait.until(EC.visibility_of_element_located(self.authorization_pass_error)).text

    def unsuccessful_authorization_email(self):
        """ Checking authorization with the invalid mail and valid password"""
        login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
        login.click()
        time.sleep(2)

        mail = self.wait.until(EC.presence_of_element_located(self.e_mail_field))
        mail.click()
        mail.send_keys('ruzifawoma@heximailcom')

        password = self.wait.until(EC.presence_of_element_located(self.pass_field))
        password.click()
        password.send_keys('qi3R8Ue4gj8g9BV')

        submit = self.wait.until(EC.visibility_of_element_located(self.submit_btn))
        submit.click()
        time.sleep(3)

        return self.wait.until(EC.visibility_of_element_located(self.authorization_mail_error)).text

    def recovery_pass(self):
        """ Checking recovery of the password """
        login = self.wait.until(EC.presence_of_element_located(self.login_btn_header))
        login.click()
        time.sleep(2)

        self.wait.until(EC.presence_of_element_located(self.forgot_pass_btn)).click()
        time.sleep(2)
        recovery_form = self.wait.until(EC.presence_of_element_located(self.mail_field_in_forgot_pass))
        recovery_form.click()
        recovery_form.send_keys('qevawenemmo-7199@yopmail.com')
        self.wait.until(EC.element_to_be_clickable(self.new_pass_btn)).click()
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located(self.close_recovery_popup)).click()

        return self.driver.current_url

        # return self.wait.until(EC.visibility_of_element_located(self.recovery_pass_succ_msg)).text
