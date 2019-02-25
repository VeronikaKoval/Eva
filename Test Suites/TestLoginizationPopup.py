from BaseTest import BaseTest
from Pages.LoginizationPopUp import Loginization


class TestLoginization(BaseTest):

    def test_login(self):
        """ Checking the presence of the pop up after clicking the login btn"""
        main_page = Loginization()
        assert main_page.login() is True

    def test_unsuccessful_authorization_pass(self):
        """ Checking authorization with the valid mail and invalid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Неправильный адрес электронной почты (email) или пароль' in main_page.unsuccessful_authorization_pass()

    def test_unsuccessful_authorization_mail(self):
        """ Checking authorization with the invalid mail and valid password and verifying the text of the error msg"""
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.unsuccessful_authorization_email()

    def test_successful_authorization(self):
        """ Checking authorization with the valid email and password and verifying the name of the account of the
         registered person"""
        main_page = Loginization()
        assert 'Doctor' in main_page.get_account_text()

    def test_recovery_unsucc(self):
        """ Checking recovery of the password with the invalid mail and verifying the text of the error"""
        main_page = Loginization()
        assert 'Пожалуйста, введите правильный адрес электронной почты' in main_page.recovery_pass_unsuccess()

    def test_recovery_pass(self):
        """ Checking recovery of the password with the valid mail and """
        main_page = Loginization()
        assert 'Если на сайте существует учётная запись с адресом cemmozosyh-0165@yopmail.com,' \
               ' Вы получите письмо со ссылкой для смены пароля.' in main_page.recovery_pass_success()