from selenium.common.exceptions import WebDriverException

from BasePage import BasePage

from BaseTest import BaseTest

from selenium.webdriver.common.by import By

from MainPageHeader import Header

class Test(BaseTest):

    def test_main_page(self):
        slaider_locator = (By.CSS_SELECTOR, 'div.header-contact div.button')
        base_page = BasePage()
        base_page.click(slaider_locator)

    def test_search_field_is_clickable(self):
        main_page = Header()
        search_locator = main_page.search_field
        # try:
        #     main_page.click(search_locator)
        # except WebDriverException:
        #     print ('Element is not clickable')
        main_page.