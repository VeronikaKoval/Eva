import pytest

from selenium.webdriver.common.by import By


# Locators
confirm_location_btn = (By.CSS_SELECTOR, 'a.block-location-action.action-yes.js-hide-location')


@pytest.fixture(scope='function')
def get_cookies(request):
    """ """
    # request.cls.driver.get('https://eva.ua/')
    # from Pages.BasePage import BasePage
    # BasePage().click(confirm_location_btn, 'Confirm suggested loc btn')
    cookies_list = request.cls.driver.get_cookies()
    print(cookies_list)
    cookies_dict = {}
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
        print(len(cookies_dict))

    # def add_cookies(self):
        cookie = {'name': 'foo', 'value': 'bar'}
        request.driver.add_cookie(cookie)
        print(len(cookie))

        # for cookie in cookies_list:
        #     self.driver.add_cookie({k: cookie[k] for k in ('name', 'value', 'domain')})