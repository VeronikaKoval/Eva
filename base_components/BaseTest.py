
from driver import Driver


class BaseTest:

    def setup(self):
        self.driver = Driver.get_webdriver()
        # self.driver.maximize_window()
        self.base_url = 'https://eva.ua/'
        # self.driver.get(self.base_url)

    def teardown(self):
        Driver.close_driver()

    def switch_to_previous_tab(self):
        """
        Switch from the current tab to previous tab
        """
        try:
            self.driver.switch_to.window(self.driver.window_handles[1])
            return self
        except:
            raise Exception('Is is impossible to switch to previous tab')

    def go_back_to_previous_tab(self):
        """
        Switching to previously opened tab in the history
        """
        try:
            self.driver.execute_script("window.history.go(-1)")
            return self
        except:
            raise Exception('Is is impossible to switch to previous tab')

    def save_screenshot(self, filename):
        """
        Saves a screenshot of the current window to a PNG image file.
        """
        self.driver.save_screenshot(filename)
        return self
