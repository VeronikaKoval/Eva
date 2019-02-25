
from singleton import Singleton


class BaseTest:

    def setup(self):
        self.driver = Singleton.get_webdriver()
        self.driver.maximize_window()
        self.base_url = 'https://eva.ua/'
        # self.driver.get(self.base_url)

    def teardown(self):
        Singleton.close_driver()
