import time

import pytest

from Pages.MainPageUpperPanel import Panel
from TestSuites.BaseTest import BaseTest
from Pages.LoginizationPopUp import LoginPopup


class TestLoginization(BaseTest):

    def setup(self):
        super(TestLoginization, self).setup()
        self.driver.get(self.base_url)
        self.main_page = Panel().open_login_popup()

    def test_registration_link(self):
        """ Checking if the register link  and 'The "Forgot password" link are visible in the login popup"""
        login_popup = LoginPopup()
        assert login_popup.is_register_link_visible() is True, 'The registration link is not visible'
        assert login_popup.is_forgot_pass_link_visible() is True, 'The "Forgot password" link is not visible or absent'

    @pytest.mark.parametrize('login, password',
                             [
                                 ('ruzifawoma@heximailcom', 'qi3R8Ue4gj8g9BV'),
                                 ('ruzifawomaheximail.com', 'qi3R8Ue4gj8g9BV'),
                                 ('«»‘~!@#$%^&*()?>,./\<][ /*<!—«», «${}»;—>', 'qi3R8Ue4gj8g9BV')
                             ])

    def test_unsuccessful_authorization_mail(self, login, password):
        """Checking authorization with the invalid mail(without ".", without "@") and valid password,
        :return: authorization error message text to verify the text of the error msg"""
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
        """ Checking authorization with the valid email and invalid password(without ".", without "@"),
        :return: authorization error message text to verify the text of the error msg"""
        login_popup = LoginPopup()
        login_popup.authorize(login, password)
        assert 'Неправильный адрес электронной почты (email) или пароль' in login_popup.get_error_text_wrong_pass(), \
            'The text of the error msg about wrong password is different or absent'

    def test_successful_authorization(self):
        """ Checking authorization with the valid email and password,
         :return: account name text to verify the name of the account of the registered person"""
        login_popup = LoginPopup()
        login_popup.authorize(login='ruzifawoma@heximail.com', password='qi3R8Ue4gj8g9BV')
        time.sleep(1)
        panel = Panel()
        assert panel.is_popup_present_after_authorization() is True, \
            'Popup after authorization is not visible or absent'

    def test_authorization_with_empty_field(self):
        """ Opening the login popup, clicking the submit bytton, without entering login and password,
        :return: authorization error message text to verify the text of the error """
        login_popup = LoginPopup()
        login_popup.authorization_with_empty_field()
        assert login_popup.get_error_text_with_empty_login_pass() == 'Это обязательное поле',\
            'Text of the error doesnt match or absent'

    # def test_unsuccessful_authorization_mail(self):
    #     """ Checking authorization with the invalid mail(without ".") and valid password,
    #      :return: authorization error message text to verify the text of the error msg"""
    #     main_page = LoginPopup()
    #     main_page.authorize(login='ruzifawoma@heximailcom', password='qi3R8Ue4gj8g9BV')
    #     assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_text_wrong_email()

    # def test_unsuccessful_authorization_email(self):
    #     """ Checking authorization with the invalid mail(without "@") and valid password,
    #              :return: authorization error message text to verify the text of the error msg"""
    #     main_page = LoginPopup()
    #     main_page.authorize(login='ruzifawomaheximail.com', password='qi3R8Ue4gj8g9BV')
    #     assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_text_wrong_email()

    # def test_unsuccessful_authorization_pass(self):
    #     """ Checking authorization with the valid mail and invalid password,
    #     :return: authorization error message text to verify the text of the error msg"""
    #     main_page = LoginPopup()
    #     main_page.authorize(login='ruzifawoma@heximail.com', password='chcciicnbcg')
    #     assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.get_error_text_wrong_pass(), \
    #         'The error text is different or absent'

    def test_recovery_unsucc(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering invalid email(without "@"),
        :return: recovery error msg text to verify the text of the error"""
        recovery_popup = self.main_page.click_forgot_pass()
        recovery_popup.recovery(mail='qevawenemmo-7199yopmail.com'), 'Mail is not entered'
        # time.sleep(2)
        assert 'Пожалуйста, введите правильный адрес электронной почты' in \
            recovery_popup.get_error_msg_recovery_wrong_email(),  'The recovery msg error text is different or absent'

    def test_recovery_success(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering valid email, :return: recovery success msg text """
        recovery_popup = self.main_page.click_forgot_pass()
        recovery_popup.recovery(mail='heltanefye@desoz.com')
        recovery_popup.close_login_popup()
        assert 'Если на сайте существует учётная запись с адресом heltanefye@desoz.com,' \
               ' Вы получите письмо со ссылкой для смены пароля.' in recovery_popup.get_recovery_success_msg_text(), \
            'The recovery success message is different or absent' #закрити попап
