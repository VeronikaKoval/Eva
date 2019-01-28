from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from singleton import Singleton

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    wait_element_time = 10

    def __init__(self):
        self.driver = Singleton.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def find_element(self, locator, element_name):
        return self.wait.until(EC.presence_of_element_located(locator), 'There is no element "{}"'.format(element_name))

    def click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.click()

    def hover_element(self, locator):
        element_to_hover = self.wait.until(EC.presence_of_element_located(locator))
        hover = ActionChains(self.driver).move_to_element(element_to_hover)
        hover.perform()
