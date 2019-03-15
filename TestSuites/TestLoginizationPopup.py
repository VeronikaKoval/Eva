import time

import pytest

from Pages.MainPageBody import Body
from Pages.MainPageUpperPanel import Panel
from TestSuites.BaseTest import BaseTest
from Pages.LoginizationPopUp import LoginPopup


class TestLoginization(BaseTest):

    def setup(self):
        super(TestLoginization, self).setup()
        self.driver.get(self.base_url)
        self.main_page = Panel().open_login_popup()

    def test_visibility_of_popup_elements(self):
        """ Checking if the email field, password field, "Submit"  btn, register link, "Stay on site" checkbox and
        'The "Forgot password" link are visible in the login popup"""
        login_popup = LoginPopup()
        assert login_popup.is_email_field_visible() is True, 'The email field is not visible'
        assert login_popup.is_pass_field_visible() is True, 'The password field is not visible'
        assert login_popup.is_submit_btn_visible() is True, 'The "Submit" button is not visible'
        assert login_popup.is_checkbox_visible() is True, 'The checkbox "Stay on site" is not visible'
        assert login_popup.is_register_link_visible() is True, 'The registration link is not visible'
        assert login_popup.is_forgot_pass_link_visible() is True, 'The "Forgot password" link is not visible or absent'

    @pytest.mark.parametrize('login, password',
                             [
                                 ('ruzifawoma@heximailcom', 'qi3R8Ue4gj8g9BV'),
                                 ('ruzifawomaheximail.com', 'qi3R8Ue4gj8g9BV'),
                                 ('«»‘~!@#$%^&*()?>,./\<][ /*<!—«», «${}»;—>', 'qi3R8Ue4gj8g9BV')
                             ])

    def test_unsuccessful_authorization_mail(self, login, password):
        """ Entering invalid mail(without ".", without "@") and valid password to check authorization,
        getting authorization error message text to verify the text of the error msg"""
        login_popup = LoginPopup()
        login_popup.authorize(login, password)
        assert 'Пожалуйста, введите правильный адрес электронной почты' in login_popup.get_error_text_wrong_email(), \
            'The text of the error msg about wrong email is different or absent'

    @pytest.mark.parametrize('login, password',
                             [
                                 ('ruzifawoma@heximail.com', 'Qi3R8Ue4gj8g9BV'),
                                 ('ruzifawoma@heximail.com', 'QI3R8UE4GJ8G9BV'),
                                 ('ruzifawoma@heximail.com', 'vfkivjiovppapcv'),
                                 ('ruzifawoma@heximail.com', '  qi3R8Ue4gj8g9BV')
                             ])

    def test_unsuccessful_authorization_password(self, login, password):
        """ Entering valid mail and invalid password to check authorization,
        getting authorization error message text to verify the text of the error msg"""
        login_popup = LoginPopup()
        login_popup.authorize(login, password)
        assert 'Неправильный адрес электронной почты (email) или пароль' in login_popup.get_error_text_wrong_pass(), \
            'The text of the error msg about wrong password is different or absent'

    def test_successful_authorization(self):
        """ Entering valid mail and valid password to check successful authorization, check whether popup
        after authorization with options is visible"""
        login_popup = LoginPopup()
        login_popup.authorize(login='ruzifawoma@heximail.com', password='qi3R8Ue4gj8g9BV')
        time.sleep(1)
        panel = Panel()
        assert panel.is_popup_visible_after_authorization() is True, \
            'Popup after authorization is not visible or absent'

    def test_authorization_with_empty_field(self):
        """ Clicking the submit button, without entering login and password to check unsuccessful authorization
         getting authorization error message text"""
        login_popup = LoginPopup()
        login_popup.authorization_with_empty_field()
        assert login_popup.get_error_text_with_empty_login_pass() == 'Это обязательное поле',\
            'Text of the error doesnt match or absent'

    def test_recovery_unsucc(self):
        """ Clicking on "Забыли пароль" btn, entering email, clicking "Получить новый пароль" btn",
        entering invalid email(without "@"), getting recovery error msg text to verify the text of the error"""
        recovery_popup = self.main_page.click_forgot_pass()
        assert recovery_popup.is_mail_in_recovery_visible() is True, 'Mail field in recovery is not visible'
        recovery_popup.recovery(mail='qevawenemmo-7199yopmail.com'), 'Mail is not entered'
        assert recovery_popup.is_get_new_pass_btn_visible() is True, '"Get new password" btn is not visible'
        # time.sleep(2)
        assert 'Пожалуйста, введите правильный адрес электронной почты' in \
            recovery_popup.get_error_msg_recovery_wrong_email(),  'The recovery msg error text is different or absent'

    def test_recovery_success(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering valid email, get recovery success message """
        recovery_popup = self.main_page.click_forgot_pass()
        recovery_popup.recovery(mail='miwixiq@getnada.com')
        login_popup = LoginPopup()
        main_page = Body()
        login_popup.close_login_popup()
        time.sleep(2)
        assert 'Если на сайте существует учётная запись с адресом miwixiq@getnada.com,' \
               ' Вы получите письмо со ссылкой для смены пароля.' in main_page.get_recovery_success_msg_text(), \
            'The recovery success message is different or absent'