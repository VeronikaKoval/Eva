from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from driver import Driver

from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    wait_element_time = 10

    def __init__(self):
        self.driver = Driver.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def find_element(self, locator, element_name):
        """ Looking for element with given locator, check if element is present
        :param locator
        :param element_name: name of element which used in error message
        :return: page element"""
        try:
            self.wait.until(EC.presence_of_element_located(locator), 'There is no element "{}"'.format(element_name))
            return self
        except:
            raise Exception('{} not found'.format(element_name))

    def click(self, locator, element_name):
        """ Looking for element with given locator, check if element is clickable and click on the element
        :param locator
        :param element_name: name of element
        :return: page element """
        required_item = self.wait.until(EC.presence_of_element_located(locator),
                                        'There is no element "{}"'.format(element_name))
        if self.element_is_clickable(locator, element_name):
            required_item.click()
        else:
            raise Exception('{} not clickable'.format(element_name))
        return self

    def hover_element(self, locator, element_name):
        """ Hovering element with given locator, check if element is visible
        :param locator
        :param element_name: name of element
        :return: element """
        element_to_hover = self.wait.until(EC.visibility_of_element_located(locator),
                                           '{} not visible'.format(element_name))
        try:
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            return self
        except:
            raise Exception('{} can not be hovered'.format(element_name))

    def element_is_clickable(self, locator, element_name):
        """ Looking for element with given locator and check if this element is enabled
        :param locator: tuple of method to search and locator
        :param element_name: name of element
        :return: 'True' if the web-element is clickable, otherwise returns 'False'
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator)), '{} not visible'.format(element_name)
            return True
        except:
            return False

    def is_element_present(self, locator, element_name):
        """ Looking for element with given locator and check if this element is present
        :param locator
        :param element_name: name of element
        :return: Returns 'True' if the web-element is present, otherwise returns 'False'"""
        try:
            self.wait.until(EC.presence_of_element_located(locator)), 'There is no element "{}"'.format(element_name)
            return True
        except:
            return False

    def is_element_visible(self, locator, element_name):
        """ Looking for element with given locator and check if this element is visible
        :param locator
        :param element_name: name of element
        :return: Returns 'True' if the web-element is visible, otherwise returns 'False'"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator)), '{} not visible'.format(element_name)
            return True
        except:
            return False

    def get_page_url(self):
        """ Getting the page url,
        :return: string: page current URL"""
        return self.driver.current_url

