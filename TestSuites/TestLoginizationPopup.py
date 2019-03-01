import pytest

from TestSuites.BaseTest import BaseTest
from Pages.LoginizationPopUp import Loginization


class TestLoginization(BaseTest):

    def setup(self):
        super(TestLoginization, self).setup()
        self.driver.get(self.base_url)

    def test_login(self):
        """ Checking the presence of the pop up after clicking the login btn"""
        main_page = Loginization()
        assert main_page.is_login_popup_present() is True, 'The login popup is absent'

    @pytest.mark.parametrize('login, password',
                             [
                                 ('ruzifawoma@heximailcom', 'qi3R8Ue4gj8g9BV'),
                                 ('ruzifawomaheximail.com', 'qi3R8Ue4gj8g9BV')
                             ])

    def test_unsuccessful_authorization_mail(self, login, password):
        """Checking authorization with the invalid mail(without ".", without "@") and valid password,
        :return: authorization error message text to verify the text of the error msg"""
        main_page = Loginization()
        main_page.authorize(login, password)
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_text_wrong_email()

    def test_successful_authorization(self):
        """ Checking authorization with the valid email and password,
         :return: account name text to verify the name of the account of the registered person"""
        main_page = Loginization()
        main_page.authorize(login='ruzifawoma@heximail.com', password='qi3R8Ue4gj8g9BV')
        assert 'Doctor' in main_page.get_account_name_text(), 'The name of the account is different or absent'

    # def test_unsuccessful_authorization_mail(self):
    #     """ Checking authorization with the invalid mail(without ".") and valid password,
    #      :return: authorization error message text to verify the text of the error msg"""
    #     main_page = Loginization()
    #     main_page.authorize(login='ruzifawoma@heximailcom', password='qi3R8Ue4gj8g9BV')
    #     assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_text_wrong_email()

    # def test_unsuccessful_authorization_email(self):
    #     """ Checking authorization with the invalid mail(without "@") and valid password,
    #              :return: authorization error message text to verify the text of the error msg"""
    #     main_page = Loginization()
    #     main_page.authorize(login='ruzifawomaheximail.com', password='qi3R8Ue4gj8g9BV')
    #     assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.get_error_text_wrong_email()

    def test_unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password,
        :return: authorization error message text to verify the text of the error msg"""
        main_page = Loginization()
        main_page.authorize(login='ruzifawoma@heximail.com', password='chcciicnbcg')
        assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.get_error_text_wrong_pass(), \
            'The error text is different or absent'

    def test_recovery_unsucc(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering invalid email(without "@"),
        :return: recovery error msg text to verify the text of the error"""
        main_page = Loginization()
        main_page.recovery_password(email='qevawenemmo-7199yopmail.com')
        assert 'Пожалуйста, введите правильный адрес электронной почты' in \
               main_page.get_error_msg_recovery_wrong_email(),  'The error text is different or absent'

    def test_recovery_success(self):
        """ Opening the login popup, clicking on "Забыли пароль" btn, entering email,
        clicking "Получить новый пароль" btn", entering valid email, :return: recovery success msg text """
        main_page = Loginization()
        main_page.recovery_password(email='cemmozosyh-0165@yopmail.com')
        assert 'Если на сайте существует учётная запись с адресом cemmozosyh-0165@yopmail.com,' \
               ' Вы получите письмо со ссылкой для смены пароля.' in main_page.get_recovery_success_msg_text(), \
            'The success message is different or absent'
