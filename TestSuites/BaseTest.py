
from singleton import Singleton


class BaseTest:

    def setup(self):
        self.driver = Singleton.get_webdriver()
        self.driver.maximize_window()
        self.base_url = 'https://eva.ua/'
        # self.driver.get(self.base_url)

    def teardown(self):
        Singleton.close_driver()

    def switch_to_previous_tab(self):
        """ Switch from the current tab to previous tab"""
        return self.driver.switch_to.window(self.driver.window_handles[1])

    def go_back_to_previous_tab(self):
        """ Switching to previously opened tab in the history"""
        return self.driver.execute_script("window.history.go(-1)")

    def save_screenshot(self, filename):
        """  Saves a screenshot of the current window to a PNG image file."""
        self.driver.save_screenshot(filename)
